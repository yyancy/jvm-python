
from .constant_pool import *


class SymRef:

  def __init__(self) -> None:
    self.cp : ConstantPool = None
    self.class_name:str = None
    from . import cls
    self.clazz: cls.Class = None

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

    