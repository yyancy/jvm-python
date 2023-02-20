from __future__ import annotations
import logging


import jvm.classpath.classpath as classpath
from ...classfile.class_file import *


from . import cls
class ClassLoader:
  cp: classpath.Classpath
  class_map: dict[str, cls.Class]

  def __init__(self, cp: classpath.Classpath) -> None:
    self.cp = cp
    self.class_map = dict()

  def load_class(self, name: str) -> cls.Class:
    clz = self.class_map.get(name)
    if clz != None:
      return clz  # has already loaded

    return self.load_non_array_class(name)

  def read_class(self, name: str) -> tuple[bytes, classpath.Entry]:
    data, entry, err = self.cp.read_class(name)
    if err != None:
      raise SystemExit(f"java.lang.ClassNotFoundException: {name}")
    return data, entry

  def define_class(self, data: bytes) -> cls.Class:
    clazz = parse_class(data)
    clazz.loader = self
    resolve_super_class(clazz)
    resolve_interfaces(clazz)
    self.class_map[clazz.name] = clazz
    return clazz

  def load_non_array_class(self, name: str) -> cls.Class:
    data, entry = self.read_class(name)
    clazz = self.define_class(data)
    link(clazz)
    logging.info(f"Loaded {name} from {entry} constant pool {clazz.constant_pool}")

    return clazz


def parse_class(data: bytes) -> cls.Class:
  cf, err = parse(data)
  if err != None:
    raise err
    raise SystemExit("java.lang.ClassFormatError")
  return cls.Class(cf)


def resolve_super_class(clazz: cls.Class):
  if clazz.name != "java/lang/Object":
    clazz.super_class = clazz.loader.load_class(clazz.super_class_name)


def resolve_interfaces(clazz: cls.Class):
  interfaceCount = len(clazz.interface_names)
  if interfaceCount > 0:
    clazz.interfaces = [clazz.loader.load_class(interface_name)
                        for interface_name in clazz.interface_names]


def link(clazz: cls.Class):
  verify(clazz)
  prepare(clazz)


def verify(clazz: cls.Class):
  # todo: verify class data
  pass


def prepare(clazz: cls.Class):
  calc_instance_field_slot_ids(clazz)
  calc_static_fields_slot_ids(clazz)
  alloc_and_init_static_vars(clazz)

from jvm.rtda.heap.field import Field
def init_static_final_var(clazz: cls.Class, field: Field):
  # assert False, f'to be implemented'
  vars = clazz.static_vars
  cp = clazz.constant_pool
  cp_index = field.const_value_index
  slot_id = field.slot_id
  
  if cp_index > 0:
    match field.descriptor:
      case 'Z'|'B'|'C'|'S'|'I':
        val:int32 = cp.get_constant(cp_index)
        vars.set_int(slot_id, val)
      case 'J':
        val:int64 = cp.get_constant(cp_index)
        vars.set_int(slot_id, val)
      case 'F':
        val:float = cp.get_constant(cp_index)
        vars.set_int(slot_id, val)
      case 'D':
        val:float = cp.get_constant(cp_index)
        vars.set_int(slot_id, val)
      case 'Ljava/lang/String;':
          assert False, 'todo'




def alloc_and_init_static_vars(clazz: cls.Class):
  from . import slots
  clazz.static_vars = slots.Slots(clazz.static_slot_count)
  for field in clazz.fields:
    if field.is_static() and field.is_final():
      init_static_final_var(clazz, field)

  

def calc_instance_field_slot_ids(clazz: cls.Class):
  # print(f"class structre {clazz.super_class=}")
  if clazz.super_class != None:
    slot_id = clazz.super_class.instance_slot_count 
  else :
    slot_id = 0

  # slot_id = clazz.super_class.instance_slot_count 
  for field in clazz.fields:
    if not field.is_static():
      field.slot_id = slot_id
      slot_id+=1
      if field.is_long_or_double():
        slot_id+=1
  
  clazz.instance_slot_count = slot_id

def calc_static_fields_slot_ids(clazz: cls.Class):
  slot_id = 0
  for field in clazz.fields:
    if field.is_static():
      field.slot_id = slot_id
      slot_id+=1
      if field.is_long_or_double():
        slot_id+=1
  
  clazz.static_slot_count = slot_id
