
from __future__ import annotations
from ...common.cons import *
from ...classfile.constant_pool import *
from ...classfile.constant_info import *
from ...classfile.class_file import *
from .access_flag import *
import cls


class ClassMember:
  access_flags: uint16
  name: str
  descriptor: str
  clazz: cls.Class

  def copy_member_info(self, member_info: MemberInfo):
    self.access_flags = member_info.access_flags
    self.name = member_info.name()
    self.descriptor = member_info.descriptor()
