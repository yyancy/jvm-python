

from jvm.rtda.frame import Frame


# public final native Class<?> getClass();
def get_class(frame: Frame):
  this = frame.local_vars.get_this()
  clazz = this.clazz.jclass
  frame.operand_stack.push_ref(clazz)

def hashcode(frame: Frame):
  this = frame.local_vars.get_this()
  val = hash(this)
  frame.operand_stack.push_int(val)
def clone(frame: Frame):
  this = frame.local_vars.get_this()
  cloneable = this.clazz.loader.load_class('java/lang/Cloneable')
  if not this.clazz.is_implements(cloneable):
    raise SystemExit(f'java.lang.CloneNotSupportedException')
  frame.operand_stack.push_ref(this.clone())