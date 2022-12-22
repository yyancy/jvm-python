from base.instruction import *
from rtda.frame import Frame


class POP(NoOperandsInstuction):
  pass

  def execute(self, frame: Frame):
    stack = frame.operand_stack
    stack.pop_slot()

class POP2(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    stack.pop_slot()
    stack.pop_slot()
