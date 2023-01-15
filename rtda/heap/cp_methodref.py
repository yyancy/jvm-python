
from .cp_memberref import *
from .method import *

class MethodRef(MemberRef):
  method: Method
  def __init__(self, cp: ConstantPool, ref_info: MethodrefConstantInfo) -> None:
    self.cp = cp
    self.copy_memberref_info(ref_info)


