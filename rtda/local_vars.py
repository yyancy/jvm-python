from .slot import Slot


class LocalVars:
  def __init__(self, max_locals: int) -> None:
    self.slots: list[Slot] = None
    if max_locals > 0:
      self.slots = [None] * max_locals

  def set_int(self, i: int, val: int):
    self.slots[i].num = val

  def get_int(self, i: int) -> int:
    return self.slots[i].num

  def set_float(self, i: int, val: float):
    self.slots[i].num = val

  def get_float(self, i: int) -> float:
    return self.slots[i].num

  def set_long(self, i: int, val: int):
    self.slots[i].num = val
    self.slots[i+1].num = val

  def get_long(self, i: int) -> int:
    return self.slots[i].num

  def set_ref(self, i: int, o: object):
    self.slots[i].ref = o

  def get_ref(self, i: int) -> object:
    return self.slots[i].ref
