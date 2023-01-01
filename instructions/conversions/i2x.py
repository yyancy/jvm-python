from ..base.instruction import *

from common.cons import *
from rtda.frame import Frame

class I2B(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    i = stack.pop_int()
    stack.push_int(i)
class I2C(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    i = stack.pop_int()
    stack.push_int(i)
class I2S(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    i = stack.pop_int()
    stack.push_int(i)
class I2L(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    i = stack.pop_int()
    stack.push_long(i)
class I2F(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    i = stack.pop_int()
    f = float(i)
    stack.push_float(f)
class I2D(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    i = stack.pop_int()
    f = float(i)
    stack.push_double(f)