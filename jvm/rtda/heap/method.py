from __future__ import annotations

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
    if code_attr != None:
      self.max_stack = code_attr.max_stacks
      self.max_locals = code_attr.max_locals
      self.code = code_attr.codes

  def is_static(self) -> bool:
    return 0 != self.access_flags & access_flag.ACC_STATIC


def new_methods(clazz: cls.Class,
                cf_methods: list[MemberInfo]) -> list[Method]:
  methods: list[Method] = []
  for m in cf_methods:
    nm = Method()
    nm.clazz = clazz
    nm.copy_member_info(m)
    nm.copy_attributes(m)
    methods.append(nm)
  return methods
