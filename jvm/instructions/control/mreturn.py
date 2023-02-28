

from jvm.instructions.base.instruction import NoOperandsInstuction
from jvm.rtda.frame import Frame


class RETURN(NoOperandsInstuction):
  def execute(self, frame: Frame):
    frame.thread.pop_frame()


class ARETURN(NoOperandsInstuction):
  def execute(self, frame: Frame):
    thread = frame.thread
    current_frame = thread.pop_frame()
    invoker_frame = thread.top_frame()
    ref = current_frame.operand_stack.pop_ref()
    invoker_frame.operand_stack.push_ref(ref)


class DRETURN(NoOperandsInstuction):
  def execute(self, frame: Frame):
    thread = frame.thread
    current_frame = thread.pop_frame()
    invoker_frame = thread.top_frame()
    val = current_frame.operand_stack.pop_double()
    invoker_frame.operand_stack.push_double(val)


class FRETURN(NoOperandsInstuction):
  def execute(self, frame: Frame):
    thread = frame.thread
    current_frame = thread.pop_frame()
    invoker_frame = thread.top_frame()
    val = current_frame.operand_stack.pop_float()
    invoker_frame.operand_stack.push_float(val)


class IRETURN(NoOperandsInstuction):
  def execute(self, frame: Frame):
    thread = frame.thread
    current_frame = thread.pop_frame()
    invoker_frame = thread.top_frame()
    ret_val = current_frame.operand_stack.pop_int()
    invoker_frame.operand_stack.push_int(ret_val)


class LRETURN(NoOperandsInstuction):
  def execute(self, frame: Frame):
    thread = frame.thread
    current_frame = thread.pop_frame()
    invoker_frame = thread.top_frame()
    val = current_frame.operand_stack.pop_long()
    invoker_frame.operand_stack.push_long(val)
