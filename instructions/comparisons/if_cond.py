from base.instruction import *
from common.cons import *
from rtda.frame import Frame


class IFEQ(BranchInstuction):
  def execute(self, frame: Frame):
    val = frame.operand_stack.pop_int()
    if val == 0:
      super.bra
class IFNE(BranchInstuction):
  pass
class IFLT(BranchInstuction):
  pass
class IFLE(BranchInstuction):
  pass
class IFGT(BranchInstuction):
  pass
class IFGE(BranchInstuction):
  pass


assert False, f'to be implemented'