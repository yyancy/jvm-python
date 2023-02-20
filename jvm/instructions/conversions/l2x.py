from ..base.instruction import *

from jvm.common.cons import *
from jvm.rtda.frame import Frame


class L2D(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    l = stack.pop_long()
    d= float(l)
    stack.push_double(d)
class L2F(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    l = stack.pop_long()
    d= float(l)
    stack.push_float(d)
class L2I(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    l = stack.pop_long()
    i= int(l)
    stack.push_int(i)