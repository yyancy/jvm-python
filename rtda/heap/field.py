from __future__ import annotations

import class_member
import cls

import access_flag
from ...classfile.class_file import *
# from ...classfile.constant_info import *
# from ...classfile.constant_pool import *
from ...common.cons import *


class Field(class_member.ClassMember):
  slot_id: int
  const_value_index: int

  def is_static(self) -> bool:
    return 0 != self.access_flags & access_flag.ACC_STATIC

  def is_final(self) -> bool:
    return 0 != self.access_flags & access_flag.ACC_FINAL

  def is_long_or_double(self) -> bool:
    return self.descriptor == "J" or self.descriptor == "D"

  def copy_attributes(self,  cf_field: MemberInfo):
    val_attr = cf_field.constant_value_attribute()
    if val_attr != None:
      self.const_value_index = val_attr.constant_value_index


def new_fields(clazz: cls.Class,
               cf_fields: list[MemberInfo]) -> list[Field]:
  fields: list[Field] = []
  for f in cf_fields:
    nf = Field()
    nf.clazz = clazz
    nf.copy_member_info(f)
    nf.copy_attributes(f)
    fields.append(nf)
  return fields
