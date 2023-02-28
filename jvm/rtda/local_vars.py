from .slot import Slot


class LocalVars:
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

  def set_ref(self, i: int, o: object):
    slot = Slot()
    slot.ref = o
    self.slots[i] = slot

  def get_ref(self, i: int) -> object:
    return self.slots[i].ref
  def set_slot(self, i:int, slot:Slot):
    self.slots[i] = slot
