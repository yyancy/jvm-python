
from ..base.instruction import *
from rtda.frame import Frame


class SWAP(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    stack.push_slot(slot1)
    stack.push_slot(slot2)
