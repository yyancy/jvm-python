from __future__ import annotations
import logging
from typing import NewType

from classpath.entry import Err

from .class_reader import *

uint8 = NewType('uint8', int)
uint16 = NewType('uint16', int)
uint32 = NewType('uint32', int)
uint64 = NewType('uint64', int)


class AttributeInfo:
  pass


class ConstantInfo:
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    self.tag = tag
    self.cp = cp

  def read_info(self, reader: ClassReader) -> None:
    raise Exception("not implemented!")


class ConstantPool:
  def __init__(self) -> None:
    self.infos: list[ConstantInfo] = [None]

  def append(self, info: ConstantInfo) -> None:
    self.infos.append(info)

  def get_constant_info(index: uint16) -> ConstantInfo:
    pass

  def get_name_and_type(index: uint16) -> tuple[str, str]:
    pass

  def get_class_name(index: uint16) -> str:
    pass

  def get_utf8(index: uint16) -> str:
    pass


CONSTANT_CLASS = 7
CONSTANT_FIELDREF = 9
CONSTANT_METHODREF = 10
CONSTANT_INTERFACE_METHODREF = 11
CONSTANT_STRING = 8
CONSTANT_INTEGER = 3
CONSTANT_FLOAT = 4
CONSTANT_LONG = 5
CONSTANT_DOUBLE = 6
CONSTANT_NAME_AND_TYPE = 12
CONSTANT_UTF8 = 1
CONSTANT_METHOD_HANDLE = 15
CONSTANT_METHOD_TYPE = 16
CONSTANT_INVOKE_DYNAMIC = 18


class DoublejConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.value: float

  def read_info(self, reader: ClassReader) -> None:
    import struct
    data = reader.read_bytes(8)
    [self.value] = struct.unpack('d', data)


class FloatConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.value: float

  def read_info(self, reader: ClassReader) -> None:
    import struct
    data = reader.read_bytes(4)
    [self.value] = struct.unpack('f', data)


class LongConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.value: int

  def read_info(self, reader: ClassReader) -> None:
    self.value = reader.read_u64()


class IntegerConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.value: int

  def read_info(self, reader: ClassReader) -> None:
    self.value = reader.read_u32()


class StringConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.string_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.string_index = reader.read_u16()


class CommonConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.class_index: uint16
    self.name_and_type_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.class_index = reader.read_u16()
    self.name_and_type_index = reader.read_u16()


class InterfaceMethodrefConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.info: ConstantInfo = CommonConstantInfo(tag, cp)

  def read_info(self, reader: ClassReader) -> None:
    self.info.read_info(reader)


class MethodrefConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.info: ConstantInfo = CommonConstantInfo(tag, cp)

  def read_info(self, reader: ClassReader) -> None:
    self.info.read_info(reader)


class FieldrefConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.info: ConstantInfo

  def read_info(self, reader: ClassReader) -> None:
    self.info.read_info(reader)


class ClassConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.name_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.name_index = reader.read_u16()


def get_constant_info(tag: int, cp: ConstantPool) -> ConstantInfo:
  info: ConstantInfo
  if tag == CONSTANT_CLASS:
    info = ClassConstantInfo(tag, cp)


def read_constant_info(reader: ClassReader, cp: ConstantPool) -> ConstantInfo:
  cp = reader.read_u8()
  pass


def read_constant_pool(reader: ClassReader) -> ConstantPool:
  counts = reader.read_u16()
  cp = ConstantPool()
  for i in range(1, counts):
    cp.append(read_constant_info(reader))
    pass


class MemberInfo:
  def __init__(self) -> None:
    self.cp: ConstantPool
    self.access_flags: uint16
    self.name_index: uint16
    self.descriptor_index: uint16
    self.attributes: list[AttributeInfo]

  def name(self) -> str:
    return self.cp.get_utf8(self.name_index)

  def descriptor(self) -> str:
    return self.cp.get_utf8(self.descriptor_index)


def read_members(reader: ClassReader, cp: ConstantPool) -> list[MemberInfo]:
  counts = reader.read_u16()
  members = [read_member(reader, cp) for i in range(counts)]
  # for i in range(counts):
  #     members[i] = read_member(reader, cp)
  return members


def read_member(reader: ClassReader, cp: ConstantPool) -> MemberInfo:
  info = MemberInfo()
  info.cp = cp
  info.access_flags = reader.read_u16()
  info.name_index = reader.read_u16()
  info.descriptor_index = reader.read_u16()
  info.attributes = read_attributes(reader, cp)


def read_members(reader: ClassReader, pool: ConstantPool) -> list[MemberInfo]:
  pass


def read_member(reader: ClassReader, pool: ConstantPool) -> MemberInfo:
  pass


def read_attributes(reader: ClassReader, pool: ConstantPool) -> list[AttributeInfo]:
  pass


class ClassFile:
  def __init__(self) -> None:
    self.magic: uint32
    self.minor_version: uint16
    self.major_version: uint16
    self.constant_pool: ConstantPool
    self.access_flags: uint16
    self.this_class: uint16
    self.super_class: uint16
    self.interfaces: list[uint16]
    self.fields: list[MemberInfo]
    self.methods: list[MemberInfo]
    self.attributes: list[AttributeInfo]

  def read(self, reader: ClassReader):
    self.read_and_check_magic(reader)
    self.read_and_check_version()

    self.constant_pool = read_constant_pool(reader)

    self.access_flags = reader.read_u16()
    self.this_class = reader.read_u16()
    self.super_class = reader.read_u16()
    self.interfaces = reader.read_u16s()
    self.fields = read_members(reader, self.constant_pool)
    self.methods = read_members(reader, self.constant_pool)
    self.attributes = read_attributes(reader)

  # check magic number
  def read_and_check_magic(self, reader: ClassReader):
    self.magic = reader.read_u32()
    if self.magic != 0xCAFEBABE:
      raise Err(
          f"java.lang.ClassFormatError: expected magic number 0xCAFEBABE, got {self.magic:0x}")

  # read and check class file version
  def read_and_check_version(self, reader: ClassReader):
    self.minor_version = reader.read_u16()
    self.major_version = reader.read_u16()
    if self.major_version == 45:
      return

    if self.major_version in [46, 47, 49, 50, 51, 52] and self.minor_version == 0:
      return
    raise Err(
        f"Unsupport class file version: {self.minor_version=} {self.major_version}")

  def class_name(self, ) -> str:
    pass

  def super_class_name(self, ) -> str:
    pass

  def interface_names(self, ) -> list[str]:
    pass


def parse(class_data: bytes) -> tuple[ClassFile, Err]:
  try:
    cr = ClassReader(class_data)
    cf = ClassFile()
    cf.read(cr)
  except Exception as e:
    logging.error(f"could not read class file: {e}")
    return None, e

  return cf, None
