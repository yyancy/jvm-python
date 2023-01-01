from ..base.instruction import *

from common.cons import *
from rtda.frame import Frame


class D2F(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    d = stack.pop_double()
    f = float(d)
    stack.push_int(f)


class D2I(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    d = stack.pop_double()
    i = int(d)
    stack.push_int(i)


class D2L(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    d = stack.pop_double()
    i = int(d)
    stack.push_long(i)
