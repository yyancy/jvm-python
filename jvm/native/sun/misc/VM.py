

from jvm.rtda.frame import Frame
from jvm.rtda.heap import string_pool
from jvm.instructions.base.method_invoke_logic import invoke_method


def initialize(frame: Frame):
  vm_class = frame.method.clazz
  saved_props = vm_class.get_ref_var('savedProps', 'Ljava/util/Properties;')
  key = string_pool.jstring(vm_class.loader, 'foo')
  val = string_pool.jstring(vm_class.loader, 'bar')
  frame.operand_stack.push_ref(saved_props)
  frame.operand_stack.push_ref(key)
  frame.operand_stack.push_ref(val)
  props_class = vm_class.loader.load_class('java/util/Properties')
  set_prop_method = props_class.get_instance_method(
      'java/util/Properties', '(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Object;')
  invoke_method(frame, set_prop_method)
