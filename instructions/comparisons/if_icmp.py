from base.instruction import *
from common.cons import *
from rtda.frame import Frame


class IF_ICMPEQ(BranchInstuction):
  pass


class IF_ICMPNE(BranchInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    v2 = stack.pop_int()
    v1 = stack.pop_int()
    if v1 != v2:
      super().branch(frame, self.offset)



class IF_ICMPLT(BranchInstuction):
  pass


class IF_ICMPLE(BranchInstuction):
  pass


class IF_ICMPGT(BranchInstuction):
  pass


class IF_ICMPGE(BranchInstuction):
  pass
