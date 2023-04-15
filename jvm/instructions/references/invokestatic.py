

from jvm.instructions.base import class_init_logic
from jvm.instructions.base.instruction import Index16Instuction
from jvm.instructions.base.method_invoke_logic import invoke_method
from jvm.rtda.frame import Frame
from jvm.rtda.heap.cp_methodref import MethodRef
import logging

class INVOKE_STATIC(Index16Instuction):
  def execute(self, frame: Frame):
    cp = frame.method.clazz.constant_pool
    method_ref: MethodRef = cp.get_constant(self.index)
    resolved_method = method_ref.resolved_method()
    if not resolved_method.is_static():
      raise SystemExit('java.lang.IncompatibleClassChangeError')
  
    clazz = resolved_method.clazz
    if not clazz.init_started:
      frame.revert_next_pc()
      class_init_logic.init_class(frame.thread, clazz)
      return

    logging.info(f'start...')
    invoke_method(frame, resolved_method)

