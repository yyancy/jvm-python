from ..base.instruction import *
from jvm.rtda.frame import Frame


class POP(NoOperandsInstuction):
  def fetch_operands(self, reader: BytecodeReader):
    pass
  

  def execute(self, frame: Frame):
    stack = frame.operand_stack
    stack.pop_slot()

class POP2(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    stack.pop_slot()
    stack.pop_slot()
