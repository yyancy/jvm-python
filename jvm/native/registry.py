

import typing
from jvm.rtda.frame import Frame


registry = dict()

def register(class_name: str, method_name: str,
             method_descriptor: str, method):
  key = f'{class_name}~{method_name}~{method_descriptor}'
  registry[key] = method


def emptyNativeMethod(frame: Frame):
  pass


def find_native_method(class_name: str, method_name: str,
                       method_descriptor: str):
  key = f'{class_name}~{method_name}~{method_descriptor}'
  val = registry.get(key)
  if val != None:
    return val
  if method_descriptor == '()V' and method_name == 'registerNatives':
    return emptyNativeMethod
  return None
