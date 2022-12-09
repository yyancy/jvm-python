
from .slot import Slot


class OperandStack:
  def __init__(self, max_stack: int) -> None:
    self.size: int = 0
    self.slots: list[Slot] = None
    if max_stack > 0:
      self.slots = [None] * max_stack

  def push_int(self, val: int):
    slot = Slot()
    slot.num = val
    self.slots[self.size] = slot
    self.size += 1

  def pop_int(self) -> int:
    self.size -= 1
    return self.slots[self.size].num

  def push_float(self, val: float):
    self.push_int(val)

  def pop_float(self) -> float:
    return self.pop_int()

  def push_long(self, val: int):
    slot = Slot()
    slot.num = val
    self.slots[self.size] = slot
    self.size += 2

  def pop_long(self) -> int:
    self.size -= 2
    return self.slots[self.size].num

  def push_double(self, val: int):
    slot = Slot()
    slot.num = val
    self.slots[self.size] = slot
    self.size += 2

  def pop_double(self) -> int:
    self.size -= 2
    return self.slots[self.size].num

  def push_ref(self, o: object):
    slot = Slot()
    slot.ref = o
    self.slots[self.size] = slot
    self.size += 1

  def pop_ref(self) -> object:
    self.size -= 1
    ref = self.slots[self.size].ref
    self.slots[self.size] = None
    return ref
