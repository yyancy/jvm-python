
from __future__ import annotations
from .object import *

class Slot:
  num: int
  ref: Object
  def __init__(self) -> None:
    self.ref = None
    self.num = 0

class Slots:
  """
   和local_vars 文件内容基本一致， 不过是内容的重复
  """
  def __init__(self, max_locals: int) -> None:
    self.slots: list[Slot] = []
    self.slots.extend(Slot() for _ in range(max_locals))

  def set_int(self, i: int, val: int):
    self.slots[i].num = val

  def get_int(self, i: int) -> int:
    # return self.slots[i].num
    slot = self.slots[i]
    return 0 if slot is None else slot.num

  def set_float(self, i: int, val: float):
    self.set_int(i, val)

  def get_float(self, i: int) -> float:
    return self.slots[i].num

  def set_long(self, i: int, val: int):
    self.slots[i].num = val
    self.slots[i+1].num = val

  def get_long(self, i: int) -> int:
    return self.slots[i].num

  def set_double(self, i:int,val:int):
    self.slots[i].num =val
    self.slots[i+1].num = val
    
  def get_double(self, i: int) -> int:
    return self.slots[i].num

  def set_ref(self, i: int, o: Object):
    self.slots[i].ref = o

  def get_ref(self, i: int) -> Object:
    slot = self.slots[i]
    return slot.ref if slot is not None else None
