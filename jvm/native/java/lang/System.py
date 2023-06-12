
import os
from jvm.instructions.base.method_invoke_logic import invoke_method
from jvm.rtda.frame import Frame, new_shim_frame
from jvm.rtda.heap import string_pool
from jvm.rtda.heap.array_object import array_copy0
from jvm.rtda.heap.object import Object
from jvm.rtda.operand_stack import OperandStack


def set_out0(frame: Frame):
  out = frame.local_vars.get_ref(0)
  sys_class = frame.method.clazz
  sys_class.set_ref_var('out', "Ljava/io/PrintStream;", out)


def array_copy(frame: Frame):
  vars = frame.local_vars
  src = vars.get_ref(0)
  src_pos = vars.get_int(1)
  dest = vars.get_ref(2)
  dest_pos = vars.get_int(3)
  length = vars.get_int(4)
  if src == None or dest == None:
    raise SystemExit("java.lang.NullPointerException")

  if not check_array_copy(src, dest):
    raise SystemExit("java.lang.ArrayStoreException")

  if (src_pos < 0 or dest_pos < 0 or length < 0
     or src_pos+length > src.array_length() or dest_pos+length > dest.array_length()):
    raise SystemExit("java.lang.IndexOutOfBoundsException")

  array_copy0(src, dest, src_pos, dest_pos, length)


def check_array_copy(src: Object, dest: Object) -> bool:
  src_class = src.clazz
  dest_class = dest.clazz

  if not src_class.is_array() or not dest_class.is_array():
    return False

  if src_class.component_class().is_primitive() or dest_class.component_class().is_primitive():
    return src_class == dest_class
  return True


def sys_props() -> dict[str:str]:
  return {
		"java.version":         "1.8.0",
		"java.vendor":          "jvm.go",
		"java.vendor.url":      "https://github.com/zxh0/jvm.go",
		"java.home":            "todo",
		"java.class.version":   "52.0",
		"java.class.path":      "todo",
		"java.awt.graphicsenv": "sun.awt.CGraphicsEnvironment",
		"os.name":              os.name,   # todo
		"os.arch":              os.name, # todo
		"os.version":           "",             # todo
		"file.separator":       "/",            # todo os.PathSeparator
		"path.separator":       ":",            # todo os.PathListSeparator
		"line.separator":       "\n",           # todo
		"user.name":            "",             # todo
		"user.home":            "",             # todo
		"user.dir":             ".",            # todo
		"user.country":         "CN",           # todo
		"file.encoding":        "UTF-8",
		"sun.stdout.encoding":  "UTF-8",
		"sun.stderr.encoding":  "UTF-8",
  }


def init_properties(frame: Frame):
  local_vars = frame.local_vars
  props = local_vars.get_ref(0)

  stack = frame.operand_stack
  stack.push_ref(props)
  # public synchronized Object setProperty(String key, String value)
  set_prop_method = props.clazz.get_instance_method(
      "setProperty", "(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Object;")
  thread = frame.thread

  __p = sys_props()
  for key, val in __p.items():
    jkey = string_pool.jstring(frame.method.clazz.loader, key)
    jval = string_pool.jstring(frame.method.clazz.loader, val)
    ops = OperandStack(3)
    ops.push_ref(props)
    ops.push_ref(jkey)
    ops.push_ref(jval)

    shim_frame = new_shim_frame(thread, ops)
    thread.push_frame(shim_frame)
    
    invoke_method(shim_frame,set_prop_method)
