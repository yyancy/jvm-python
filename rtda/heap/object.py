
from __future__ import annotations
import io
import json
import sys
import cls
from .slots import *


class Object:
  clazz: cls.Class
  fields: Slots

  def __init__(self, clazz: cls.Class) -> None:
    self.clazz = clazz
    self.fields = Slots(clazz.instance_slot_count)
