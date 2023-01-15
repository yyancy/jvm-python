from .cp_memberref import *
from .field import *

class FieldRef(MemberRef):
  field: Field
  def __init__(self, cp: ConstantPool, ref_info: FieldrefConstantInfo) -> None:
    self.cp = cp
    self.copy_memberref_info(ref_info)


