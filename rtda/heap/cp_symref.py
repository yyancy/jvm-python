
from .constant_pool import *


class SymRef:
  cp : ConstantPool
  class_name:str
  clazz: cls.Class

  def resolved_class(self)-> cls.Class:
    if self.clazz == None:
      self.resolve_class_ref()
    
    return self.clazz

  def resolve_class_ref(self):
    d = self.cp.clazz
    c = d.loader.load_class(self.class_name)
    if not c.is_accessible_to(d):
      raise SystemExit("java.lang.IllegalAccessError")
    self.clazz = c

    