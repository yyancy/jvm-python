
from jvm.rtda.frame import Frame


# public native int arrayBaseOffset(Class<?> type);
# (Ljava/lang/Class;)I
def array_base_offset(frame: Frame):
  stack = frame.operand_stack
  stack.push_int(0)  # todo


# public native int arrayIndexScale(Class<?> type);
# (Ljava/lang/Class;)I
def arrayIndexScale(frame: Frame):
  stack = frame.operand_stack
  stack.push_int(1)  # todo


def addressSize(frame: Frame):
  stack = frame.operand_stack
  stack.push_int(8)  # todo unsafe.Sizeof(int)


def objectFieldOffset(frame: Frame):
  _vars = frame.local_vars
  jfield = _vars.get_ref(1)

  offset = jfield.get_intvar('slot', 'I')
  frame.operand_stack.push_long(offset)