from __future__ import annotations

from .class_member import *

from ...classfile.class_file import *
from ...classfile.constant_info import *
from ...classfile.constant_pool import ConstantPool as cf_ConstantPool
from ...common.cons import *


class Constant:
  def __init__(self) -> None:
    self.value = None


from jvm.rtda.heap.cls import Class
class ConstantPool:
  clazz: Class
  consts: list[Constant]

  def __init__(self, clazz: Class, consts: list[Constant]) -> None:
    self.clazz = clazz
    self.consts = consts

  def get_constant(self, index: int) -> Constant:
    c = self.consts[index]
    if c != None:
      return c
    raise SystemExit(f"No constants at index {index}")


def new_class_ref(rt_cp: ConstantPool, class_info: ConstantInfo):
  from . import cp_classref
  return  cp_classref.ClassRef(rt_cp, class_info)
  # assert False, f'to be implemented'


def new_field_ref(rt_cp: ConstantPool, class_info: ConstantInfo):
  from . import cp_fieldref
  return cp_fieldref.FieldRef(rt_cp, class_info)
  assert False, f'to be implemented'


def new_method_ref(rt_cp: ConstantPool, class_info: ConstantInfo):
  from . import cp_methodref
  return cp_methodref.MethodRef(rt_cp, class_info)
  # assert False, f'to be implemented'


def new_interface_method_ref(rt_cp: ConstantPool, class_info: ConstantInfo):
  from . import cp_interface_methodref
  return cp_interface_methodref.InterfaceMethodRef(rt_cp, class_info)
  # assert False, f'to be implemented'


def new_constant_pool(clazz: cls.Class, cf_cp: cf_ConstantPool) -> ConstantPool:
  consts = [Constant() for _ in range(len(cf_cp))]
  rt_cp = ConstantPool(clazz, consts)
  i = 1
  while i< len(cf_cp):
    cp_info = cf_cp.get_constant_info(i)
    match cp_info:
      case IntegerConstantInfo() as int_info:
        consts[i] = int_info.value
      case FloatConstantInfo() as float_info:
        consts[i] = float_info.value
      case LongConstantInfo() as long_info:
        consts[i] = long_info.value
        i += 1  # accoupy 2 spaces
      case DoubleConstantInfo() as double_info:
        consts[i] = double_info.value
        i += 1  # accoupy 2 spaces
      case StringConstantInfo() as string_info:
        consts[i] = string_info.string()
      case ClassConstantInfo() as class_info:
        consts[i] = new_class_ref(rt_cp, class_info)

      case FieldrefConstantInfo() as fieldref_info:
        consts[i] = new_field_ref(rt_cp, fieldref_info)

      case MethodrefConstantInfo() as methodref_info:
        consts[i] = new_method_ref(rt_cp, methodref_info)

      case InterfaceMethodrefConstantInfo() as methodref_info:
        consts[i] = new_interface_method_ref(rt_cp, methodref_info)
    i+=1
  return rt_cp
