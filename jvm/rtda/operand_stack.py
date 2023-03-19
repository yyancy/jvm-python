
from .slot import Slot
import logging


class OperandStack:
  def __init__(self, max_stack: int) -> None:
    self.size: int = 0
    self.slots: list[Slot] = None
    if max_stack > 0:
      # print(f"max stack = {max_stack}")
      self.slots = [None] * max_stack

  def push_int(self, val: int):
    slot = Slot()
    slot.num = val
    logging.debug(f"slots size = {len(self.slots)=}, current size = {self.size=}")
    self.slots[self.size] = slot
    self.size += 1

  def pop_int(self) -> int:
    self.size -= 1
    logging.debug(f'pop ref = {self.size=}')
    return self.slots[self.size].num

  def push_float(self, val: float):
    self.push_int(val)

  def pop_float(self) -> float:
    logging.debug(f'pop ref = {self.size=}')
    return self.pop_int()

  def push_long(self, val: int):
    slot = Slot()
    slot.num = val
    self.slots[self.size] = slot
    self.size += 2

  def pop_long(self) -> int:
    self.size -= 2
    logging.debug(f'pop ref = {self.size=}')
    return self.slots[self.size].num

  def push_double(self, val: int):
    slot = Slot()
    slot.num = val
    self.slots[self.size] = slot
    self.size += 2

  def pop_double(self) -> int:
    self.size -= 2
    logging.debug(f'pop ref = {self.size=}')
    return self.slots[self.size].num

  def push_ref(self, o: object):
    slot = Slot()
    slot.ref = o
    logging.debug(f"push ref {o=} slots size = {len(self.slots)=}, current size = {self.size=}")
    
    self.slots[self.size] = slot
    self.size += 1

  def pop_ref(self) -> object:
    self.size -= 1
    ref = self.slots[self.size].ref
    logging.debug(f'pop ref = {ref=} {self.size=}')
    # self.slots[self.size] = None
    return ref

  def push_slot(self, slot: Slot):
    self.slots[self.size] = slot
    self.size += 1

  def pop_slot(self) -> Slot:
    self.size -= 1
    logging.debug(f'pop ref = {self.size=}')
    return self.slots[self.size]

  def get_ref_from_top(self, i: int)-> object:
    return self.slots[self.size - i -1].ref
