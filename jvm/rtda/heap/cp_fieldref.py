from . import cls
from .cp_memberref import *
from .field import *


class FieldRef(MemberRef):
  field: Field = None

  def __init__(self, cp: ConstantPool, ref_info: FieldrefConstantInfo) -> None:
    super().__init__()
    self.cp = cp
    self.copy_memberref_info(ref_info)

  def resolved_field(self) -> Field:
    if self.field == None:
      self.resolve_field_ref()
    return self.field

  def resolve_field_ref(self):
    d = self.cp.clazz
    c = self.resolved_class()
    logging.debug(f'{c.name=}')
    field = lookup_field(c, self.name, self.descriptor)
    logging.debug(f'{field=}')
    if field == None:
      raise SystemExit("java.lang.NoSuchFieldError")
    if not field.is_accessible_to(d):
      raise SystemExit("java.lang.IllegalAccessError")

    self.field = field

  # def is_accessible_to(self, other: cls.Class) -> bool:


def lookup_field(clazz: cls.Class, name: str, descriptor: str) -> Field:
  for field in clazz.fields:
    if field.name == name and field.descriptor == descriptor:
      return field

  for iface in clazz.interfaces:
    field = lookup_field(iface, name, descriptor)
    if field != None:
      return field

  if clazz.super_class != None:
    return lookup_field(clazz.super_class, name, descriptor)

  return None
