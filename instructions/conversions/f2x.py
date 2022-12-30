from base.instruction import *

from common.cons import *
from rtda.frame import Frame

# convert float to double
class F2D(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    f = stack.pop_float()