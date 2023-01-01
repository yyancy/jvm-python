
from ..base.instruction import *

from rtda.frame import Frame


class DNEG(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_double()
    stack.push_double(-val)


class FNEG(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_float()
    stack.push_float(-val)


class INEG(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_int()
    stack.push_int(-val)


class LNEG(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_long()
    stack.push_long(-val)
