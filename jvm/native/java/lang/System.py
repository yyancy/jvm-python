
from jvm.rtda.frame import Frame
from jvm.rtda.heap.array_object import array_copy0
from jvm.rtda.heap.object import Object


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
