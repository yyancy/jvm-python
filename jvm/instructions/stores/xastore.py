from jvm.instructions.base.instruction import NoOperandsInstuction
from jvm.rtda.frame import Frame
from jvm.rtda.heap.object import Object


def check_not_none(ref: Object):
  if ref == None:
    raise SystemExit(f'java.lang.NullPointerException')


def check_index(len: int, index: int):
  if index < 0 or index >= len:
    raise SystemExit(f'ArrayIndexOutofBoundException')


class AASTORE(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    ref = stack.pop_ref()
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    refs = arr_ref.refs()
    check_index(len(refs), index)
    refs[index] = ref


class BASTORE(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_int()
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    byte_list = arr_ref.bytes()
    check_index(len(byte_list), index)
    byte_list[index] = val


class CASTORE(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_int()
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    chars = arr_ref.chars()
    check_index(len(chars), index)
    chars[index] = val


class DASTORE(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_double()
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    doubles = arr_ref.doubles()
    check_index(len(doubles), index)
    doubles[index] = val


class FASTORE(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_float()
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    floats = arr_ref.floats()
    check_index(len(floats), index)
    floats[index] = val


class IASTORE(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_int()
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    ints = arr_ref.ints()
    check_index(len(ints), index)
    ints[index] = val


class LASTORE(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_long()
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    longs = arr_ref.longs()
    check_index(len(longs), index)
    longs[index] = val


class SASTORE(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    val = stack.pop_int()
    index = stack.pop_int()
    arr_ref = stack.pop_ref()
    check_not_none(arr_ref)
    shorts = arr_ref.shorts()
    check_index(len(shorts), index)
    shorts[index] = val
