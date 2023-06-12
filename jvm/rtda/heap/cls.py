from __future__ import annotations



from ...common.cons import *
from . import method
# from ...classfile.constant_pool import *
# from ...classfile.constant_info import *
# from ...classfile.class_file import *
from .access_flag import *
from .class_loader import ClassLoader
from .field import *
from .object import Object
from .object import new_array_object
from .slots import *
# from jvm.rtda.heap.constant_pool import new_constant_pool, ConstantPool




def get_source_file(cf: ClassFile) -> str:
  sf_attr = cf.source_file_attribute()
  return sf_attr.filename() if sf_attr is not None else 'Unknonw'


class Class:
  access_flags: uint16
  name: str
  super_class_name: str
  interface_names: list[str]
  constant_pool: ConstantPool
  fields: list[Field]
  methods: list[method.Method]
  loader: ClassLoader
  super_class: Class
  interfaces: list[Class]
  instance_slot_count: uint32
  static_slot_count: uint32
  static_vars: Slots

  def __eq__(self, other) -> bool:
    if isinstance(other, self.__class__):
      return self.__dict__ == other.__dict__
    else:
      return False

  def __init__(self, cf: ClassFile) -> None:
    self.access_flags: uint16 = 0
    self.name: str = None
    self.super_class_name: str = None
    self.interface_names: list[str] = None
    self.constant_pool: ConstantPool = None
    self.fields: list[Field] = None
    self.methods: list[method.Method] = None
    self.loader: ClassLoader = None
    self.super_class: Class = None
    self.interfaces: list[Class] = []
    self.instance_slot_count: uint32 = 0
    self.static_slot_count: uint32 = 0
    self.static_vars: Slots = None
    self.source_file: str = None
    self.jclass = None  # Object
    if cf is None:
      return
    self.access_flags = cf.access_flags
    self.init_started: bool = False
    self.name = cf.class_name()
    self.source_file = get_source_file(cf)
    self.super_class_name = cf.super_class_name()
    self.interface_names = cf.interface_names()
    from jvm.rtda.heap.constant_pool import new_constant_pool
    self.constant_pool = new_constant_pool(
        self, cf.constant_pool)

    self.fields = new_fields(self, cf.fields)
    self.methods = method.new_methods(self, cf.methods)
    self.super_class = None

  def start_init(self):
    self.init_started = True

  def component_class(self) -> Class:
    component_class_name = get_component_class_name(self.name)
    return self.loader.load_class(component_class_name)
  
  def set_ref_var(self, field_name:str, field_descriptor:str, ref):
    field = self.get_field(field_name,field_descriptor, True)
    self.static_vars.set_ref(field.slot_id, ref)

  def is_primitive(self) -> bool:
    val = primitive_types.get(self.name)
    return val != None

  def new_array(self, count: int) -> Object:
    if not self.is_array():
      raise SystemExit(f'Not array class: {self.name}')
    match self.name:
      case '[Z' | '[B' | '[C' | '[S' | '[I' | '[J' | '[F' | '[D':
        arr = [0]*count
        return new_array_object(self, arr)
      case _:
        arr = [None]*count
        return new_array_object(self, arr)

  def is_array(self) -> bool:
    return self.name[0] == '['

  def array_class(self) -> Class:
    array_class_name = get_array_class_name(self.name)
    return self.loader.load_class(array_class_name)

  def get_clinit_method(self) -> Method:
    return self.get_static_method('<clinit>', '()V')

  def is_public(self) -> bool:
    return 0 != self.access_flags & ACC_PUBLIC

  def is_accessible_to(self, other: Class) -> bool:
    return self.is_public() or self.get_package_name() == other.get_package_name()

  def get_package_name(self) -> str:
    i = self.name.rfind("/")
    if i != -1:
      return self.name[:i]
    return ""

  def is_subclass_of(self, other: Class) -> bool:
    c = self.super_class
    while c != None:
      if c == other:
        return True
      c = c.super_class
    return False

  def is_superclass_of(self, other: Class) -> bool:
    return other.is_subclass_of(self)

  def is_implements(self, iface: Class) -> bool:
    c = self
    while c != None:
      for i in c.interfaces:
        if i == iface or i.is_subinterface_of(iface):
          return True
      c = c.super_class
    return False

  def is_subinterface_of(self, iface: Class) -> bool:
    for suerinterface in self.interfaces:
      if suerinterface == iface or suerinterface.is_subinterface_of(iface):
        return True
    return False

  def is_assignable_from(self, other: Class) -> bool:
    s, t = other, self
    if s == t:
      return True

    if not s.is_array():
      if not s.is_interface():
        if not t.is_interface():
          return s.is_subclass_of(t)
        else:
          return s.is_implements(t)
      else:
        if not t.is_interface():
          return t.is_jlobject()
        else:
          return t.is_super_interface_of(s)
    else:
      if not t.is_array():
        if not t.is_interface():
          return t.is_jlobject()
        else:
          return t.is_jlcloneable() or t.is_jioserializable()
      else:
        sc = s.component_class()
        tc = t.component_class()
        return sc == tc or tc.is_assignable_from(sc)
    return False

  def is_public(self) -> bool:
    return 0 != self.access_flags & ACC_PUBLIC

  def is_protected(self) -> bool:
    return 0 != self.access_flags & ACC_PROTECTED

  def is_private(self) -> bool:
    return 0 != self.access_flags & ACC_PRIVATE

  def is_static(self) -> bool:
    return 0 != self.access_flags & ACC_STATIC

  def is_final(self) -> bool:
    return 0 != self.access_flags & ACC_FINAL

  def is_synthetic(self) -> bool:
    return 0 != self.access_flags & ACC_SYNTHETIC

  def is_interface(self) -> bool:
    return 0 != self.access_flags & ACC_INTERFACE

  def is_super(self) -> bool:
    return 0 != self.access_flags & ACC_SUPER

  def is_abstract(self) -> bool:
    return 0 != self.access_flags & ACC_ABSTRACT

  def is_annotation(self) -> bool:
    return 0 != self.access_flags & ACC_ANNOTATION

  def is_enum(self) -> bool:
    return 0 != self.access_flags & ACC_ENUM

  def new_object(self) -> Object:
    return Object(self)

  def get_main_method(self) -> method.Method:
    return self.get_static_method('main', "([Ljava/lang/String;)V")

  def get_method(self,name: str, descriptor: str, is_static:bool)-> method.Method:
    c = self
    while c is not None:
      for method in c.methods:
        if (method.is_static() == is_static
            and method.name ==name and method.descriptor == descriptor):
          return method
      
      c = c.super_class
    
    return None


  def get_instance_method(self, name: str, descriptor: str)->method.Method:
    return self.get_method(name, descriptor, False)

  def get_static_method(self, name: str, descriptor: str) -> method.Method:
    return self.get_method(name, descriptor, True)

  def is_jlobject(self) -> bool:
    return self.name == 'java/lang/Object'

  def is_jlcloneable(self) -> bool:
    return self.name == 'java/lang/Cloneable'

  def is_jioserializable(self) -> bool:
    return self.name == 'java/io/Serializable'

  def is_super_interface_of(self, iface: Class) -> bool:
    return iface.is_subinterface_of(self)

  def java_name(self) -> str:
    return self.name.replace('/', '.')

  def get_field(self, name: str, descriptor: str, is_static: bool) -> Field:
    c = self
    while c != None:
      for field in c.fields:
        if (field.is_static() == is_static
                and field.name == name and field.descriptor == descriptor):
          return field

      c = c.super_class
  
  def get_fields(self, public_only:bool) -> list[Field]:
    if public_only:
      return [field for field in self.fields if field.is_public()]
    else:
      return self.fields
  
  def get_constructor(self, descriptor:str)->method.Method:
    return self.get_instance_method("<init>", descriptor)

  def get_constructors(self, publicOnly:bool) -> list[method.Method]:
    return [
        method for method in self.methods
        if method.is_constructor() and (not publicOnly or method.is_public())
    ]


primitive_types = {
    'void': 'V',
    'boolean': 'Z',
    'byte': 'B',
    'short': 'S',
    'int': 'I',
    'long': 'J',
    'char': 'C',
    'float': 'F',
    'double': 'D',
}


def to_descriptor(class_name: str) -> str:
  if class_name[0] == '[':
    return class_name
  d = primitive_types.get(class_name)
  if d != None:
    return d
  return f'L{class_name};'


def get_array_class_name(class_name: str) -> str:
  return f'[{to_descriptor(class_name)}'


def get_component_class_name(class_name: str) -> str:
  if class_name[0] == '[':
    component_type_descriptor = class_name[1:]
    return to_classname(component_type_descriptor)

  raise SystemExit(f'Not array: {class_name}')


def to_classname(descriptor: str) -> str:
  if descriptor[0] == '[':  # array
    return descriptor

  if descriptor[0] == 'L':  # object
    return descriptor[1: len(descriptor)-1]

  for class_name, d in primitive_types.items():
    if d == descriptor:
      return class_name

  raise SystemExit(f'Invalid descriptor: {descriptor}')
