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
from .slots import *


from .constant_pool import *
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

  def __init__(self, cf: ClassFile) -> None:
    self.access_flags = cf.access_flags
    self.name = cf.class_name()
    self.super_class_name = cf.super_class_name()
    self.interface_names = cf.interface_names()
    self.constant_pool = new_constant_pool(
        self, cf.constant_pool)

    self.fields = new_fields(self, cf.fields)
    self.methods = method.new_methods(self, cf.methods)
    self.super_class = None

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

    if not t.is_interface():
      return s.is_subclass_of(t)
    else:
      return s.is_implements(t)

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

  def get_static_method(self, name: str, descriptor: str) -> method.Method:
    for method in self.methods:
      if method.is_static() and method.name == name and method.descriptor == descriptor:
        return method
    return None
