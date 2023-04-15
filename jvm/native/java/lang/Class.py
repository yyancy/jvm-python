

from jvm.rtda.frame import Frame
from jvm.rtda.heap import cls
from jvm.rtda.heap import string_pool
import logging

def get_primitive_class(frame: Frame):
  logging.info('coming')
  name_obj = frame.local_vars.get_ref(0)
  name = string_pool.pystring(name_obj)
  loader = frame.method.clazz.loader
  clazz = loader.load_class(name).jclass
  frame.operand_stack.push_ref(clazz)


# private native String getName0();
def getName0(frame: Frame):
  this = frame.local_vars.get_this()
  clazz: cls.Class = this.extra
  name = clazz.java_name()
  name_obj = string_pool.jstring(clazz.loader, name)
  frame.operand_stack.push_ref(name_obj)
  

# private static native boolean desiredAssertionStatus0(Class<?> clazz);
def desired_assertion_status0(frame :Frame):
  frame.operand_stack.push_bool(False)
