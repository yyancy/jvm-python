from ..base.instruction import *

from jvm.rtda.frame import Frame
from ...rtda.heap import constant_pool
from ...rtda.heap import cp_classref
from ...rtda.heap import object
from ...rtda.heap.cp_classref import ClassRef


class CHECK_CAST(Index16Instuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    ref = stack.pop_ref()
    # FUCKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
    stack.push_ref(ref)
    if ref == None:
      return

    cp = frame.method.clazz.constant_pool
    class_ref: ClassRef = cp.get_constant(self.index)
    clazz = class_ref.resolved_class()
    if not ref.is_instance_of(clazz):
      raise SystemExit('java.lang.ClassCastException')
