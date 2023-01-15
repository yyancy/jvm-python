
from __future__ import annotations
import io
import json
import sys
import cls
from .slots import *

class Object:
  clazz: cls.Class
  fields: Slots
