
from __future__ import annotations

# from .cls import *

from ...classfile.zxcv import *
# from ...classfile.constant_info import *
# from ...classfile.constant_pool import *
from ...common.cons import *
from .access_flag import *


class ClassMember:
  access_flags: uint16
  name: str
  descriptor: str


  def copy_member_info(self, member_info: MemberInfo):
    self.access_flags = member_info.access_flags
    self.name = member_info.name()
    self.descriptor = member_info.descriptor()
    self.signature = ""
    self.annotation_data:bytes = [] #// RuntimeVisibleAnnotations_attribute
    from .cls import Class
    self.clazz: Class

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

  def is_accessible_to(self, d: Class) -> bool:
    if self.is_public():
      return True

    c = self.clazz
    if self.is_protected:
      return d == c or d.is_subclass_of(c) or c.get_package_name() == d.get_package_name()

    if not self.is_private():
      return c.get_package_name() == d.get_package_name()

    return d == c
