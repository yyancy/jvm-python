
#  []*Class => Class[]
from jvm.rtda.heap import string_pool
from jvm.rtda.heap.array_object import NewByteArray
from jvm.rtda.heap.class_loader import ClassLoader
from jvm.rtda.heap.cls import Class
from jvm.rtda.heap.object import Object


def toClassArr(loader :ClassLoader, classes :Class) ->Object:
  arrLen = len(classes) if classes is not None else 0

  classArrClass = loader.load_class("java/lang/Class").array_class()
  classArr = classArrClass.new_array(arrLen)

  if arrLen > 0:
    classObjs = classArr.refs()
    for i, clazz in enumerate(classes):
      classObjs[i] = clazz.jclass()
  return classArr


# []byte => byte[]
def toByteArr(loader :ClassLoader, goBytes:bytes) ->Object:
  if goBytes is not None:
    jBytes = castUint8sToInt8s(goBytes)
    return NewByteArray(loader, jBytes)
  
  return None

def castUint8sToInt8s(goBytes:bytes)-> bytes:
  return goBytes


def getSignatureStr(loader:ClassLoader, signature:str) -> Object:
  return string_pool.jstring(loader, signature) if signature != "" else None
