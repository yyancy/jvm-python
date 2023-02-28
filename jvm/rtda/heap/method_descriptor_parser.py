from jvm.rtda.heap.method_descriptor import MethodDescriptor

from jvm.common.cons import *


def parse_method_descriptor(descriptor: str) -> MethodDescriptor:
  method_parser = MethodDescriptorParser()
  return method_parser.parse(descriptor)


class MethodDescriptorParser:
  def __init__(self) -> None:
    self.raw: str = None
    self.offset: int = 0
    self.parsed: MethodDescriptor = None

  def parse(self, descriptor: str) -> MethodDescriptor:
    self.raw = descriptor
    self.parsed = MethodDescriptor([], None)
    self.start_params()
    self.parse_param_types()
    self.end_params()
    self.parse_return_type()
    self.finish()
    return self.parsed

  def cause_panic(self):
    raise SystemExit(f'BAD descriptor {self.raw}')

  def start_params(self):
    if self.read_uint8() != '(':
      self.cause_panic()

  def end_params(self):
    if self.read_uint8() != ')':
      self.cause_panic()

  def parse_param_types(self):
    while True:
      t = self.parse_field_type()
      if t != "":
        self.parsed.parameter_types.append(t)
      else:
        return

  def parse_field_type(self) -> str:
    match self.read_uint8():
      case 'B':
        return "B"
      case 'C':
        return "C"
      case 'D':
        return "D"
      case 'F':
        return "F"
      case 'I':
        return "I"
      case 'J':
        return "J"
      case 'S':
        return "S"
      case 'Z':
        return "Z"
      case 'L':
        return self.parse_object_type()
      case '[':
        return self.parse_array_type()
      case _:
        self.unread_uint8()
        return ""

  def parse_object_type(self) -> str:
    unread = self.raw[self.offset:]
    try:
      semicolon_index = unread.index(';')
      obj_start = self.offset-1
      obj_end = self.offset + semicolon_index + 1
      self.offset = obj_end
      descriptor = self.raw[obj_start:obj_end]
      return descriptor
    except ValueError:
      self.cause_panic()

  def parse_array_type(self) -> str:
    arr_start = self.offset-1
    self.parse_field_type()
    arr_end = self.offset
    descriptor = self.raw[arr_start:arr_end]
    return descriptor

  def parse_return_type(self):
    if self.read_uint8() == 'V':
      self.parsed.return_type = 'V'
      return

    self.unread_uint8()
    t = self.parse_field_type()
    if t != '':
      self.parsed.return_type = t
      return
    self.cause_panic()

  def finish(self):
    if self.offset != len(self.raw):
      self.cause_panic()

  def read_uint8(self) -> uint8:
    b = self.raw[self.offset]
    self.offset += 1
    return b

  def unread_uint8(self):
    self.offset -= 1
