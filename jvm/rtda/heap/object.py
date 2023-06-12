
from __future__ import annotations
import io
import json
import sys
from .import cls
from .slots import *


def new_array_object(clazz: cls.Class, data) -> Object:
  o = Object(clazz)
  o.data = data
  return o


class Object:
  clazz: cls.Class
  data: object
  extra: object

  def __init__(self, clazz: cls.Class) -> None:
    self.clazz = clazz
    self.data = Slots(clazz.instance_slot_count)
    self.extra = None

  def is_instance_of(self, clazz: cls.Class) -> bool:
    return clazz.is_assignable_from(self.clazz)

  def fields(self) -> Slots:
    return self.data

  def bytes(self) -> list[int]:
    return self.data

  def shorts(self) -> list[int]:
    return self.data

  def ints(self) -> list[int]:
    return self.data

  def chars(self) -> list[int]:
    return self.data

  def floats(self) -> list[float]:
    return self.data

  def doubles(self) -> list[float]:
    return self.data

  def refs(self) -> list[Object]:
    return self.data

  def set_refvar(self, name: str, descriptor: str, ref: Object):
    field = self.clazz.get_field(name, descriptor, False)
    slots: Slots = self.data
    slots.set_ref(field.slot_id, ref)

  def get_refvar(self, name: str, descriptor: str) -> Object:
    field = self.clazz.get_field(name, descriptor, False)
    slots: Slots = self.data
    return slots.get_ref(field.slot_id)
  
  def set_intvar(self, name: str, descriptor: str, val: int):
    field = self.clazz.get_field(name, descriptor, False)
    slots: Slots = self.data
    slots.set_int(field.slot_id, val)
  def get_intvar(self, name: str, descriptor: str) -> Object:
    field = self.clazz.get_field(name, descriptor, False)
    slots: Slots = self.data
    return slots.get_int(field.slot_id)


  def array_length(self) -> int:
    match self.data:
      case list() as arr:
        return len(arr)
      case bytes() as arr:
        return len(arr)
      case _:
        raise Exception(f'Not array!')

  def clone_data(self):
    match self.data:
      case list():
        length = len(self.data)
        new_data = [0] * length
        for i, v in enumerate(self.data):
          new_data[i] = v
        return new_data
      case Slots() as s:
        length = len(s.slots)
        new_data = Slots(length)
        for i, v in enumerate(s.slots):
          new_data.slots[i] = v
          return new_data

  def clone(self) -> Object:
    o = Object(self.clazz)
    o.data = self.clone_data()
    return o
