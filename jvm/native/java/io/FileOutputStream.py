

import os
import sys
from jvm.rtda.frame import Frame


def cast_int8s_to_uint8s(b):
  return b


def write_bytes(frame: Frame):
  local_vars = frame.local_vars
  b = local_vars.get_ref(1)
  off = local_vars.get_int(2)
  length = local_vars.get_int(3)
  # append = vars.get_bool(4)
  j_bytes = b.data
  py_bytes = cast_int8s_to_uint8s(j_bytes)
  py_bytes = py_bytes[off:off+length]
  sys.stdout.buffer.write(py_bytes)
