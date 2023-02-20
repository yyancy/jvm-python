
from __future__ import annotations
from .object import *

class Slot:
  num: int
  ref: Object
  def __init__(self) -> None:
    self.ref = None

class Slots:
  """
   和local_vars 文件内容基本一致， 不过是内容的重复
  """
  def __init__(self, max_locals: int) -> None:
    self.slots: list[Slot] = None
    if max_locals > 0:
      self.slots = [None] * max_locals

  def set_int(self, i: int, val: int):
    slot = Slot()
    slot.num = val
    self.slots[i] = slot

  def get_int(self, i: int) -> int:
    return self.slots[i].num

  def set_float(self, i: int, val: float):
    self.set_int(i, val)

  def get_float(self, i: int) -> float:
    return self.slots[i].num

  def set_long(self, i: int, val: int):
    slot = Slot()
    slot.num = val
    self.slots[i] = slot
    self.slots[i+1] = slot

  def get_long(self, i: int) -> int:
    return self.slots[i].num

  def set_double(self, i:int,val:int):
    slot = Slot()
    slot.num = val
    self.slots[i] = slot
    self.slots[i+1] = slot
    
  def get_double(self, i: int) -> int:
    return self.slots[i].num

  def set_ref(self, i: int, o: Object):
    slot = Slot()
    slot.ref = o
    self.slots[i] = slot

  def get_ref(self, i: int) -> Object:
    slot = self.slots[i]
    if slot !=None:
      return slot.ref
    return None
