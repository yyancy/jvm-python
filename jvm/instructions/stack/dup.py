from ..base.instruction import *
from jvm.rtda.frame import Frame


#  Duplicate the top operand stack value
class DUP(NoOperandsInstuction):

  def execute(self, frame: Frame):
    stack = frame.operand_stack
    slot = stack.pop_slot()
    stack.push_slot(slot)
    stack.push_slot(slot)


#  Duplicate the top operand stack value and insert two values down
class DUP_X1(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    stack.push_slot(slot1)
    stack.push_slot(slot2)
    stack.push_slot(slot1)


#  Duplicate the top operand stack value and insert two or three values down
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


#  Duplicate the top one or two operand stack values
class DUP2(NoOperandsInstuction):
  def execute(self, frame: Frame):
    # assert False, f"To be implemented. a little bit complicated..."
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    stack.push_slot(slot2)
    stack.push_slot(slot1)
    stack.push_slot(slot2)
    stack.push_slot(slot1)


#  Duplicate the top one or two operand stack values and insert two or three values down
class DUP2_X1(NoOperandsInstuction):
  def execute(self, frame: Frame):
    # assert False, f"To be implemented. a little bit complicated..."
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    slot3 = stack.pop_slot()
    stack.push_slot(slot2)
    stack.push_slot(slot1)
    stack.push_slot(slot3)
    stack.push_slot(slot2)
    stack.push_slot(slot1)


#  Duplicate the top one or two operand stack values and insert two, three, or four values down
class DUP2_X2(NoOperandsInstuction):
  def execute(self, frame: Frame):
    # assert False, f"To be implemented. a little bit complicated..."
    stack = frame.operand_stack
    slot1 = stack.pop_slot()
    slot2 = stack.pop_slot()
    slot3 = stack.pop_slot()
    slot4 = stack.pop_slot()

    stack.push_slot(slot2)
    stack.push_slot(slot1)
    stack.push_slot(slot4)
    stack.push_slot(slot3)
    stack.push_slot(slot2)
    stack.push_slot(slot1)
