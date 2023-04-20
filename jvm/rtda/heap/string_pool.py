
from jvm.rtda.heap.class_loader import ClassLoader
from jvm.rtda.heap.object import Object

interned_strings: dict = {}


def jstring(loader: ClassLoader, s: str) -> Object:
  interned_str = interned_strings.get(s)
  if interned_str != None:
    return interned_str
  chars = string_to_utf16(s)
  jchars = Object(loader.load_class('[C'))
  jchars.data = chars
  jstr = loader.load_class('java/lang/String').new_object()
  jstr.set_refvar('value', '[C', jchars)
  interned_strings[s] = jstr
  return jstr


def intern_string(jstr: Object) -> Object:
  pystr = pystring(jstr)
  interned_str = interned_strings.get(pystr)
  if interned_str != None:
    return interned_str

  interned_strings[pystr] = jstr
  return jstr


def string_to_utf16(s: str) -> list:
  return list(s)


def utf16_to_string(s: list) -> str:
  for i, v in enumerate(s):
    if isinstance(v, int):
      s[i]= chr(v)
  return ''.join(s)


def pystring(jstr: Object) -> str:
  char_arr = jstr.get_refvar('value', '[C')
  return utf16_to_string(char_arr.chars())
