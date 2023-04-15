from __future__ import annotations

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
    if code_attr != None:
      self.max_stack = code_attr.max_stacks
      self.max_locals = code_attr.max_locals
      self.code = code_attr.codes

  def calc_arg_slot_count(self, param_types:list[str]):
    for param_type in param_types:
      self.arg_slot_count += 1
      if param_type == 'J' or param_type == 'D':
        self.arg_slot_count += 1

    if not self.is_static():  # this arg
      self.arg_slot_count += 1

  def is_static(self) -> bool:
    return 0 != self.access_flags & access_flag.ACC_STATIC

  def is_native(self) -> bool:
    return 0 != self.access_flags & access_flag.ACC_NATIVE
  
  def inject_code_attribute(self,
                            return_type:str):
    self.max_stack = 4
    self.max_locals = self.arg_slot_count
    match return_type[0]:
      case 'V':
        self.code = [0xfe, 0xb1] # return
      case 'D':
        self.code = [0xfe, 0xaf] # dreturn
      case 'F':
        self.code = [0xfe, 0xae] # freturn
      case 'J':
        self.code = [0xfe, 0xad] # lreturn
      case 'L'|'[':
        self.code = [0xfe, 0xb0] # areturn
      case _:
        self.code = [0xfe, 0xac] # ireturn
        


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
  method.calc_arg_slot_count(md.parameter_types)
  if method.is_native():
    method.inject_code_attribute(md.return_type)
  return method
