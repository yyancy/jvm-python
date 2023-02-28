from __future__ import annotations
import logging
from .constant_info import *
from jvm.common.cons import *
import types

cp_type = types.SimpleNamespace()
cp_type.CONSTANT_CLASS: int = 7
cp_type.CONSTANT_FIELDREF: int = 9
cp_type.CONSTANT_METHODREF: int = 10
cp_type.CONSTANT_INTERFACE_METHODREF: int = 11
cp_type.CONSTANT_STRING: int = 8
cp_type.CONSTANT_INTEGER: int = 3
cp_type.CONSTANT_FLOAT: int = 4
cp_type.CONSTANT_LONG: int = 5
cp_type.CONSTANT_DOUBLE: int = 6
cp_type.CONSTANT_NAME_AND_TYPE: int = 12
cp_type.CONSTANT_UTF8: int = 1
cp_type.CONSTANT_METHOD_HANDLE: int = 15
cp_type.CONSTANT_METHOD_TYPE: int = 16
cp_type.CONSTANT_INVOKE_DYNAMIC: int = 18

class ConstantPool:
  def __init__(self) -> None:
    self.infos: list[ConstantInfo] = [None]

  def __len__(self):
    return len(self.infos) 
  

  def append(self, info: ConstantInfo) -> None:
    self.infos.append(info)

  def get_constant_info(self, index: uint16) -> ConstantInfo:
    try:
      return self.infos[index]
    except Exception as e:
      raise Exception(f"invalid index {index}", e)

  def get_name_and_type(self, index: uint16) -> tuple[str, str]:
    ci = self.get_constant_info(index)
    sci: NameAndTypeConstantInfo = ci
    name = self.get_utf8(sci.name_index)
    _type = self.get_utf8(sci.descriptor_index)
    return name, _type

  def get_class_name(self, index: uint16) -> str:
    ci = self.get_constant_info(index)
    # print(f"{index=} {ci=}")
    sci: ClassConstantInfo = ci
    return self.get_utf8(sci.name_index)

  def get_utf8(self, index: uint16) -> str:
    ci = self.get_constant_info(index)
    sci: Utf8ConstantInfo = ci
    # print(f"{index=} sci type = {sci=} -----------------")
    return sci.value




def get_constant_info(tag: int, cp: ConstantPool) -> ConstantInfo:
  info: ConstantInfo
  if tag == cp_type.CONSTANT_CLASS:
    info = ClassConstantInfo(tag, cp)


def read_constant_info(reader: ClassReader, cp: ConstantPool) -> ConstantInfo:
  tag = reader.read_u8()
  ci: ConstantInfo
  match(tag):
    case cp_type.CONSTANT_CLASS:
      ci = ClassConstantInfo(tag, cp)
    case cp_type.CONSTANT_FIELDREF:
      ci = FieldrefConstantInfo(tag, cp)
    case cp_type.CONSTANT_METHODREF:
      ci = MethodrefConstantInfo(tag, cp)
    case cp_type.CONSTANT_INTERFACE_METHODREF:
      ci = InterfaceMethodrefConstantInfo(tag, cp)
    case cp_type.CONSTANT_STRING:
      ci = StringConstantInfo(tag, cp)
    case cp_type.CONSTANT_INTEGER:
      ci = IntegerConstantInfo(tag, cp)
    case cp_type.CONSTANT_FLOAT:
      ci = FloatConstantInfo(tag, cp)
    case cp_type.CONSTANT_LONG:
      ci = LongConstantInfo(tag, cp)
    case cp_type.CONSTANT_DOUBLE:
      ci = DoubleConstantInfo(tag, cp)
    case cp_type.CONSTANT_NAME_AND_TYPE:
      ci = NameAndTypeConstantInfo(tag, cp)
    case cp_type.CONSTANT_UTF8:
      ci = Utf8ConstantInfo(tag, cp)
    case cp_type.CONSTANT_METHOD_HANDLE:
      ci = MethodHandleConstantInfo(tag, cp)
    case cp_type.CONSTANT_METHOD_TYPE:
      ci = MethodTypeConstantInfo(tag, cp)
    case cp_type.CONSTANT_INVOKE_DYNAMIC:
      ci = InvokeDynamicConstantInfo(tag, cp)
    case _:
      raise Exception(f"unknown tag {tag:x}")
  ci.read_info(reader)
  return ci


def read_constant_pool(reader: ClassReader) -> ConstantPool:
  counts = reader.read_u16()
  # print(f'-------------constant pool size = {counts}-----------------')
  cp = ConstantPool()
  i = 1
  while i < counts:
    ci = read_constant_info(reader,cp)
    cp.append(ci)
    if isinstance(ci, (LongConstantInfo, DoubleConstantInfo)):  # 占用2个index
      cp.append(None)
      i += 1
    i += 1

  return cp