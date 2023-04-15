

from jvm.rtda.frame import Frame


# public final native Class<?> getClass();
def get_class(frame: Frame):
  this = frame.local_vars.get_this()
  clazz = this.clazz.jclass
  frame.operand_stack.push_ref(clazz)