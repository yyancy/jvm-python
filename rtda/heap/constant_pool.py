from __future__ import annotations

import class_member
import cls

from ...classfile.class_file import *
from ...classfile.constant_info import *
from ...classfile.constant_pool import ConstantPool as cf_ConstantPool
from ...common.cons import *


class Constant:
  pass


class ConstantPool:
  clazz: cls.Class
  consts: list[Constant]

  def __init__(self, clazz: cls.Class, consts: list[Constant]) -> None:
    self.clazz = clazz
    self.consts = consts
  
  def get_constant(self, index: int)-> Constant:
    c = self.consts[index]
    if c != None:
      return c
    raise SystemExit(f"No constants at index {index}")

def new_class_ref(rt_cp: ConstantPool, class_info: ConstantInfo):
  assert False, f'to be implemented'
def new_field_ref(rt_cp: ConstantPool, class_info: ConstantInfo):
  assert False, f'to be implemented'

def new_method_ref(rt_cp: ConstantPool, class_info: ConstantInfo):
  assert False, f'to be implemented'
def new_interface_method_ref(rt_cp: ConstantPool, class_info: ConstantInfo):
  assert False, f'to be implemented'
def new_constant_pool(clazz: cls.Class, cf_cp : cf_ConstantPool)-> ConstantPool:
  consts = [Constant() for _ in len(cf_cp)]
  rt_cp = ConstantPool(clazz, consts)
  for i in len(cf_cp):
    cp_info = cf_cp.get_constant_info(i)
    match cp_info:
      case IntegerConstantInfo() as int_info:
        consts[i] = int_info.value
      case FloatConstantInfo() as float_info:
        consts[i] = float_info.value
      case LongConstantInfo() as long_info:
        consts[i] = long_info.value
        i += 1 # accoupy 2 spaces
      case DoubleConstantInfo() as double_info:
        consts[i] = double_info.value
        i += 1 # accoupy 2 spaces
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