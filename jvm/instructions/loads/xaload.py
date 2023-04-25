from jvm.instructions.base.instruction import NoOperandsInstuction
from jvm.rtda.frame import Frame
from jvm.rtda.heap.object import Object


def check_not_none(ref: Object):
  if ref is None:
    raise SystemExit('java.lang.NullPointerException')


def check_index(len: int, index: int):
  if index < 0 or index >= len:
    raise SystemExit(f'ArrayIndexOutofBoundException')


class AALOAD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    refs = arr_ref.refs()
    check_index(len(refs), index)
    stack.push_ref(refs[index])


class BALOAD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    byte_list = arr_ref.bytes()
    check_index(len(byte_list), index)
    stack.push_int(int(byte_list[index]))


class CALOAD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    chars = arr_ref.chars()
    check_index(len(chars), index)
    stack.push_int(ord(chars[index]))


class DALOAD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    doubles = arr_ref.doubles()
    check_index(len(doubles), index)
    stack.push_double(doubles[index])


class FALOAD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    floats = arr_ref.floats()
    check_index(len(floats), index)
    stack.push_float(floats[index])


class IALOAD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    ints = arr_ref.ints()
    check_index(len(ints), index)
    stack.push_int(ints[index])


class LALOAD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    longs = arr_ref.longs()
    check_index(len(longs), index)
    stack.push_long(longs[index])


class SALOAD(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    shorts = arr_ref.shorts()
    check_index(len(shorts), index)
    stack.push_int(shorts[index])
