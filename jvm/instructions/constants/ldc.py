from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object
from ...rtda.heap.cp_fieldref import FieldRef


def ldc(frame: Frame, index: int):
  stack = frame.operand_stack
  cp = frame.method.clazz.constant_pool
  c = cp.get_constant(index)
  match c:
    case int():
      stack.push_int(c)
    case float():
      stack.push_float(c)
    # case str:
    # case ClassRef:
    case _:
      raise SystemExit('todo: ldc')

  # assert False, f"need to be implemented: 6.6.5"


class LDC(Index8Instuction):
  def execute(self, frame: Frame):
    ldc(frame, self.index)


class LDC_W(Index8Instuction):
  def execute(self, frame: Frame):
    ldc(frame, self.index)


class LDC2_W(Index8Instuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    cp = frame.method().clazz.constant_pool
    c = cp.get_constant(self.index)
    match c:
      case int():
        stack.push_long(c)
      case float():
        stack.push_double(c)
    # case str:
    # case ClassRef:
      case _:
        raise SystemExit('java.lang.ClassFormatError')

    # assert f"need to be implemented: 6.6.5"
