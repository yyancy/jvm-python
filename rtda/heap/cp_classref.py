
from .cp_symref import *


class ClassRef(SymRef):
  def __init__(self, cp: ConstantPool, class_info: ClassConstantInfo) -> None:
    self.cp = cp
    self.class_name = class_info.name()
