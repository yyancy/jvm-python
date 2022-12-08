
from .slot import Slot


class OperandStack:
  def __init__(self, max_stack: int) -> None:
    self.size: int
    self.slots: list[Slot] = None
    if max_stack > 0:
      self.slots = [None] * max_stack

  def push_int(self, val: int):
    self.slots[self.size].num = val
    self.size += 1

  def pop_int(self) -> int:
    self.size -= 1
    return self.slots[self.size].num

  def push_float(self, val: float):
    self.push_int(val)

  def pop_float(self) -> float:
    return self.pop_int()

  def push_long(self, val: int):
    self.slots[self.size].num = val
    self.size += 2

  def pop_long(self) -> int:
    self.size -= 2
    return self.slots[self.size].num

  def push_double(self, val: int):
    self.slots[self.size].num = val
    self.size += 2

  def pop_double(self) -> int:
    self.size -= 2
    return self.slots[self.size].num

  def set_ref(self, o: object):
    self.slots[self.size].ref = o
    self.size += 1

  def get_ref(self) -> object:
    self.size -= 1
    return self.slots[self.size].ref
