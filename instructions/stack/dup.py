from ..base.instruction import *
from rtda.frame import Frame


class DUP(NoOperandsInstuction):

  def execute(self, frame: Frame):
    stack = frame.operand_stack
    slot = stack.pop_slot()
    stack.push_slot(slot)
    stack.push_slot(slot)


class DUP_X1(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    stack.push_slot(slot1)
    stack.push_slot(slot2)
    stack.push_slot(slot1)


class DUP_X2(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    slot3 = stack.pop_slot()
    stack.push_slot(slot1)
    stack.push_slot(slot3)
    stack.push_slot(slot2)
    stack.push_slot(slot1)


class DUP2(NoOperandsInstuction):
  def execute(self, frame: Frame):
    assert False, f"To be implemented. a little bit complicated..."
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    stack.push_slot(slot2)
    stack.push_slot(slot1)
    stack.push_slot(slot2)
    stack.push_slot(slot1)


class DUP2_X1(NoOperandsInstuction):
  def execute(self, frame: Frame):
    assert False, f"To be implemented. a little bit complicated..."
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    slot3 = stack.pop_slot()
    stack.push_slot(slot2)
    stack.push_slot(slot1)
    stack.push_slot(slot3)
    stack.push_slot(slot2)
    stack.push_slot(slot1)


class DUP2_X2(NoOperandsInstuction):
  def execute(self, frame: Frame):
    assert False, f"To be implemented. a little bit complicated..."
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    slot3 = stack.pop_slot()
    slot4 = stack.pop_slot()

    stack.push_slot(slot4)
    stack.push_slot(slot3)
    stack.push_slot(slot2)
    stack.push_slot(slot1)
