
import struct

from jvm.rtda.frame import Frame


def floatToBits(f):
  s = struct.pack('>f', f)
  return struct.unpack('>l', s)[0]


def bitsToFloat(b):
  s = struct.pack('>l', b)
  return struct.unpack('>f', s)[0]


def float_to_raw_int_bits(frame: Frame):
  value = frame.local_vars.get_float(0)
  bits = floatToBits(value)
  frame.operand_stack.push_int(int(bits))


def int_bits_to_float(frame: Frame):
  bits = frame.local_vars.get_int(0)
  value = bitsToFloat(bits)
  frame.operand_stack.push_float(value)
