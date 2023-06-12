from __future__ import annotations

from jvm.rtda.heap.class_name_helper import toClassName

# from .cls import Class

from . import access_flag
from ...classfile.class_file import *
# from ...classfile.constant_info import *
# from ...classfile.constant_pool import *
from ...common.cons import *


from .class_member import ClassMember
class Field(ClassMember):
  slot_id: int
  const_value_index: int
  def __init__(self) -> None:
    super().__init__()
    self.slot_id = 0
    self.const_value_index = 0

  def is_static(self) -> bool:
    return 0 != self.access_flags & access_flag.ACC_STATIC

  def is_final(self) -> bool:
    return 0 != self.access_flags & access_flag.ACC_FINAL

  def is_long_or_double(self) -> bool:
    return self.descriptor in ["J", "D"]

  def copy_attributes(self,  cf_field: MemberInfo):
    val_attr = cf_field.constant_value_attribute()
    if val_attr != None:
      self.const_value_index = val_attr.constant_value_index
  
  def type(self)->Class:
    className = toClassName(self.descriptor)
    return self.clazz.loader.load_class(className)


def new_fields(clazz: Class,
               cf_fields: list[MemberInfo]) -> list[Field]:
  fields: list[Field] = []
  for f in cf_fields:
    nf = Field()
    nf.clazz = clazz
    nf.copy_member_info(f)
    nf.copy_attributes(f)
    fields.append(nf)
  return fields
