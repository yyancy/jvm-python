from ..base.instruction import *

from common.cons import *
from rtda.frame import Frame

# convert float to double
class F2D(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    f = stack.pop_float()
    stack.push_double(f)

class F2I(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    f = stack.pop_float()
    i = int(f)
    stack.push_int(i)
class F2L(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    f = stack.pop_float()
    i = int(f)
    stack.push_long(i)
