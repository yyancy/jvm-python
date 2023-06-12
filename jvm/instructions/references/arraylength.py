

from jvm.instructions.base.instruction import NoOperandsInstuction
from jvm.rtda.frame import Frame


class ARRAY_LENGTH(NoOperandsInstuction):
  def execute(self, frame: Frame):
    stack = frame.operand_stack
    arr_ref = stack.pop_ref()
    if arr_ref is None:
      raise Exception(f'java.lang.NullPointerException')
    arr_len = arr_ref.array_length()
    stack.push_int(arr_len)
