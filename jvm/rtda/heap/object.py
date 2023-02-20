
from __future__ import annotations
import io
import json
import sys
from .import cls
from .slots import *


class Object:
  clazz: cls.Class
  fields: Slots

  def __init__(self, clazz: cls.Class) -> None:
    self.clazz = clazz
    self.fields = Slots(clazz.instance_slot_count)

  def is_instance_of(self, clazz :cls.Class)-> bool:
    return clazz.is_assignable_from(self.clazz)
