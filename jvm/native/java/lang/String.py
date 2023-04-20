


from jvm.rtda.frame import Frame
from jvm.rtda.heap import string_pool


def intern(frame: Frame):
  this = frame.local_vars.get_this()
  interned = string_pool.intern_string(this)
  frame.operand_stack.push_ref(interned)