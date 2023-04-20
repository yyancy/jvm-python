import struct

from jvm.rtda.frame import Frame


def floatToBits(f):
  s = struct.pack('>d', f)
  return struct.unpack('>q', s)[0]


def bitsToFloat(b):
  s = struct.pack('>q', b)
  return struct.unpack('>d', s)[0]


def double_to_raw_long_bits(frame: Frame):
  value = frame.local_vars.get_double(0)
  bits = floatToBits(value)
  frame.operand_stack.push_long(int(bits))


def long_bits_to_double(frame: Frame):
  bits = frame.local_vars.get_long(0)
  value = bitsToFloat(bits)
  frame.operand_stack.push_double(value)
