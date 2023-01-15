from __future__ import annotations
from ...common.cons import *
from ...classfile.constant_pool import *
from ...classfile.constant_info import *
from ...classfile.class_file import *
from .access_flag import *
from .slots import *
from .field import *

class Class:
  access_flags: uint16
  name: str
  super_class_name: str
  interface_names: list[str]
  constant_pool: ConstantPool
  fields: list[Field]
  methods: list[Method]
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
    self.constant_pool = asdf

    self.fields = new_fields(self, cf.fields)
    self.methods = new_methods(self, cf.methods)

  def is_public(self) -> bool:
    return 0 != self.access_flags & ACC_PUBLIC
