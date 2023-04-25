

from jvm.instructions.base.instruction import NoOperandsInstuction
from jvm.native.java.lang.Throwable import StackTraceElement
from jvm.rtda.frame import Frame
from jvm.rtda.heap.object import Object
from jvm.rtda.thread import Thread
from jvm.rtda.heap import string_pool


class ATHROW(NoOperandsInstuction):
  def execute(self, frame: Frame):
    ex = frame.operand_stack.pop_ref()
    if ex is None:
      raise SystemExit('java.lang.NullPointerException')
    thread = frame.thread
    if not find_and_goto_exception_handler(thread, ex):
      handle_uncaugtht_exception(thread, ex)


def handle_uncaugtht_exception(thread: Thread, ex: Object) -> bool:
  thread.clear_stack()
  jmsg = ex.get_refvar("detailMessage", "Ljava/lang/String;")
  pymsg = string_pool.pystring(jmsg)
  print(f'{ex.clazz.java_name()}: {pymsg}')
  # assert False, f'to be implemented'
  
  stes: list[StackTraceElement] = ex.extra
  for e in stes:
    print(f'\tat {e}')




def find_and_goto_exception_handler(thread: Thread, ex: Object) -> bool:
  while True:
    frame = thread.current_frame()
    pc = frame.next_pc - 1
    handler_pc = frame.method.find_exception_handler(ex.clazz, pc)
    if handler_pc > 0:
      stack = frame.operand_stack
      stack.clear()
      stack.push_ref(ex)
      frame.set_next_pc(handler_pc)
      return True
    thread.pop_frame()
    if thread.is_stack_empty():
      break
  return False
