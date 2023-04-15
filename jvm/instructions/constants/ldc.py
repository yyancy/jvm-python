import logging
from ..base.instruction import *
import jvm.rtda.heap.string_pool as string_pool
from jvm.rtda.heap import cp_classref
from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import object
from ...rtda.heap.cp_fieldref import FieldRef
import pprint

def ldc(frame: Frame, index: int):
  stack = frame.operand_stack
  cp = frame.method.clazz.constant_pool
  c = cp.get_constant(index)
  clazz = frame.method.clazz
  match c:
    case int():
      stack.push_int(c)
    case float():
      stack.push_float(c)
    case str():
      interned_str = string_pool.jstring(clazz.loader, c)
      stack.push_ref(interned_str)
    case cp_classref.ClassRef():
      class_ref:cp_classref.ClassRef = c
      class_obj = class_ref.resolved_class().jclass
      stack.push_ref(class_obj)
    case _:
      raise SystemExit('todo: ldc')

  # assert False, f"need to be implemented: 6.6.5"


class LDC(Index8Instuction):
  def execute(self, frame: Frame):
    ldc(frame, self.index)


class LDC_W(Index16Instuction):
  def execute(self, frame: Frame):
    ldc(frame, self.index)


class LDC2_W(Index16Instuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    cp = frame.method.clazz.constant_pool
    # logging.info(f'{cp.consts=} {self.index=}')
    c = cp.get_constant(self.index)
    # print(f'{c=}')
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
