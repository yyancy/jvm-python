from ...rtda.frame import Frame
from ...rtda.thread import Thread
from ...rtda.heap.method import Method


def invoke_method(invoke_frame: Frame, method: Method):
  thread: Thread = invoke_frame.thread
  new_frame = thread.new_frame(method)
  thread.push_frame(new_frame)
  arg_slot_slot = method.arg_slot_count
  if arg_slot_slot > 0:
    for i in range(arg_slot_slot-1, -1, -1):
      slot = invoke_frame.operand_stack.pop_slot()
      new_frame.local_vars.set_slot(i, slot)

  # hack
  if method.is_native():
    if method.name == 'registerNatives':
      thread.pop_frame()
    else:
      raise SystemExit(
          f'native method: {method.clazz.name}.{method.name}{method.descriptor}')
