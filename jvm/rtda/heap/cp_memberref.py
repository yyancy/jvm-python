
from .cp_symref import *


class MemberRef(SymRef):
  name: str
  descriptor: str
  
  def __init__(self) -> None:
    super().__init__()
  
  def copy_memberref_info(self, ref_info: MemberrefConstantInfo):
    self.class_name = ref_info.class_name()
    self.name, self.descriptor = ref_info.name_and_descriptor()
