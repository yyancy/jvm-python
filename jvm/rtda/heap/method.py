from __future__ import annotations
from jvm.rtda.heap.class_name_helper import toClassName
from jvm.rtda.heap.exception_table import ExceptionTable

from jvm.rtda.heap.method_descriptor_parser import parse_method_descriptor

from . import cls

from .import access_flag
from ...classfile.class_file import *
# from ...classfile.constant_info import *
# from ...classfile.constant_pool import *
from ...common.cons import *


from .class_member import ClassMember


class Method(ClassMember):
  max_stack: uint32
  max_locals: uint32
  code: bytes
  clazz: cls.Class

  def copy_attributes(self, cf_method: MemberInfo):
    code_attr = cf_method.code_attribute()
    self.arg_slot_count = 0
    self.max_stack = 0
    self.max_locals = 0
    self.exception_table = None
    self.line_number_table: LineNumberTableAttrInfo = None
    self.exceptions :ExceptionsAttributeInfo = None
    if code_attr != None:
      self._extracted_from_copy_attributes_10(code_attr, cf_method)

  # TODO Rename this here and in `copy_attributes`
  def _extracted_from_copy_attributes_10(self, code_attr, cf_method:MemberInfo):
    self.max_stack = code_attr.max_stacks
    self.max_locals = code_attr.max_locals
    self.code = code_attr.codes
    self.line_number_table = code_attr.line_number_table_attribute()
    self.exception_table = ExceptionTable(code_attr.exception_table, self.clazz.constant_pool)
    self.exceptions = cf_method.exceptions_attribute()
    self.annotationData = cf_method.runtime_visible_annotations_attribute_data()
    self.parameterAnnotationData = cf_method.runtime_visible_parameter_annotations_attribute_data()
    self.annotationDefaultData = cf_method.annotation_default_attribute_data()

    # TODO: 

  def find_exception_handler(self, ex_class: cls.Class, pc: int) -> int:
    handler = self.exception_table.find_exception_handler(ex_class, pc)
    return handler.handler_pc if handler is not None else -1

  def get_line_number(self, pc: int) -> int:
    if self.is_native():
      return -2
    if self.line_number_table is None:
      return -1
    return self.line_number_table.get_line_number(pc)

  def calc_arg_slot_count(self, param_types: list[str]):
    for param_type in param_types:
      self.arg_slot_count += 1
      if param_type in ['J', 'D']:
        self.arg_slot_count += 1

    if not self.is_static():  # this arg
      self.arg_slot_count += 1

  def is_static(self) -> bool:
    return 0 != self.access_flags & access_flag.ACC_STATIC

  def is_native(self) -> bool:
    return 0 != self.access_flags & access_flag.ACC_NATIVE

  def inject_code_attribute(self,
                            return_type: str):
    self.max_stack = 4
    self.max_locals = self.arg_slot_count
    match return_type[0]:
      case 'V':
        self.code = [0xfe, 0xb1]  # return
      case 'D':
        self.code = [0xfe, 0xaf]  # dreturn
      case 'F':
        self.code = [0xfe, 0xae]  # freturn
      case 'J':
        self.code = [0xfe, 0xad]  # lreturn
      case 'L' | '[':
        self.code = [0xfe, 0xb0]  # areturn
      case _:
        self.code = [0xfe, 0xac]  # ireturn

  def is_constructor(self) -> bool:
    return not self.is_static() and self.name == "<init>"

  def is_clinit(self) -> bool:
    return self.is_static() and self.name == "<clinit>"

#  reflection
  def parameter_types(self) -> list[Class]:
    if self.arg_slot_count == 0:
      return None

    paramTypes = self.parsedDescriptor.parameter_types
    paramClasses = []
    for paramType in paramTypes:
      paramClassName = toClassName(paramType)
      paramClasses.append(self.clazz.loader.load_class(paramClassName))

    return paramClasses

  def  ReturnType(self) -> cls.Class:
    returnType = self.parsedDescriptor.return_type
    returnClassName = toClassName(returnType)
    return self.clazz.loader.load_class(returnClassName)
  
  def exception_types(self) -> list[Class]:
    if self.exceptions is None:
      return None


    exIndexTable = self.exceptions.index_tables
    exClasses = []
    cp = self.clazz.constant_pool

    for exIndex in exIndexTable:
      classRef = cp.get_constant(int(exIndex))
      exClasses.append(classRef.resolved_class())


    return exClasses



def new_methods(clazz: cls.Class,
                cf_methods: list[MemberInfo]) -> list[Method]:
  methods: list[Method] = []
  for m in cf_methods:
    nm = new_method(clazz, m)
    methods.append(nm)
  return methods


def new_method(clazz: cls.Class,
               cf_method: MemberInfo) -> Method:
  method = Method()
  method.clazz = clazz
  method.copy_member_info(cf_method)
  method.copy_attributes(cf_method)
  md = parse_method_descriptor(method.descriptor)
  method.parsedDescriptor =md

  method.calc_arg_slot_count(md.parameter_types)
  if method.is_native():
    method.inject_code_attribute(md.return_type)
  return method
