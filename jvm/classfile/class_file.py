from __future__ import annotations

import logging
import types
from jvm.common.cons import *
from jvm.classpath.entry import Err

from .class_reader import *
from .constant_pool import *


class AttributeInfo:
  def __init__(self, name_index: uint16, length: uint32, cp: ConstantPool) -> None:
    self.__cp: ConstantPool = cp
    self.attribute_name_index: uint16 = name_index
    self.attribute_length: uint32 = length
    self.data: bytes

  def cp(self) -> ConstantPool:
    return self.__cp

  def read_info(self, reader: ClassReader) -> None:
    raise Exception("not implemented!")


class SyntheticAttributeInfo(AttributeInfo):
  def __init__(self, name_index: uint16, length: uint32, cp: ConstantPool) -> None:
    super().__init__(name_index, length, cp)

  def read_info(self, reader: ClassReader) -> None:
    pass


class DeprecatedAttributeInfo(AttributeInfo):
  def __init__(self, name_index: uint16, length: uint32, cp: ConstantPool) -> None:
    super().__init__(name_index, length, cp)

  def read_info(self, reader: ClassReader) -> None:
    pass


class UnparsedAttributeInfo(AttributeInfo):
  def __init__(self, name_index: uint16, length: uint32, cp: ConstantPool) -> None:
    super().__init__(name_index, length, cp)
    self.data: bytes

  def read_info(self, reader: ClassReader) -> None:
    self.data = reader.read_bytes(self.attribute_length)


class LineNumberTableAttrInfo(AttributeInfo):
  def __init__(self, name_index: uint16, length: uint32, cp: ConstantPool) -> None:
    super().__init__(name_index, length, cp)
    self.table_length: uint16
    self.data: bytes

  def read_info(self, reader: ClassReader) -> None:
    self.data = reader.read_bytes(self.attribute_length)
    # self.table_length = reader.read_u16()
    # self.data = reader.read_bytes(self.table_length)


class ConstantValueAttributeInfo(AttributeInfo):
  def __init__(self, name_index: uint16, length: uint32, cp: ConstantPool) -> None:
    super().__init__(name_index, length, cp)
    self.constant_value_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.constant_value_index = reader.read_u16()


class SourceFileAttributeInfo(AttributeInfo):
  def __init__(self, name_index: uint16, length: uint32, cp: ConstantPool) -> None:
    super().__init__(name_index, length, cp)
    self.sourcefile_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.sourcefile_index = reader.read_u16()


class ExceptionsAttributeInfo(AttributeInfo):
  def __init__(self, name_index: uint16, length: uint32, cp: ConstantPool) -> None:
    super().__init__(name_index, length, cp)
    # self.number_of_exceptions: uint16
    self.index_tables: list[uint16]

  def read_info(self, reader: ClassReader) -> None:
    # self.data = reader.read_bytes(self.attribute_length)
    # self.number_of_exceptions = reader.read_u16()
    self.index_tables = reader.read_u16s()

class ExceptionTableEntry:
  def __init__(self,start_pc, end_pc, handler_pc, catch_type) -> None:
    self.start_pc:uint16 = start_pc
    self.end_pc:uint16 = end_pc
    self.handler_pc:uint16 = handler_pc
    self.catch_type:uint16 = catch_type

class CodeAttributeInfo(AttributeInfo):
  def __init__(self, name_index: uint16, length: uint32, cp: ConstantPool) -> None:
    super().__init__(name_index, length, cp)
    self.max_stacks: uint16
    self.max_locals: uint16
    self.code_length: uint32
    self.codes: bytes
    self.exception_table_length: uint16
    self.exception_table: list[ExceptionTableEntry]
    self.attributes: list[AttributeInfo]

  def read_info(self, reader: ClassReader) -> None:
    self.max_stacks = reader.read_u16()
    self.max_locals = reader.read_u16()
    self.code_length = reader.read_u32()
    self.codes = reader.read_bytes(self.code_length)
    self.exception_table_length = reader.read_u16()
    self.exception_table = []
    for _ in range(self.exception_table_length):
      start_pc = reader.read_u16()
      end_pc = reader.read_u16()
      handler_pc = reader.read_u16()
      catch_type = reader.read_u16()
      self.exception_table.append(ExceptionTableEntry(start_pc,end_pc,handler_pc, catch_type))

    # self.exception_table = reader.read_bytes(self.exception_table_length)
    self.attributes = read_attributes(reader, self.cp())


class MemberInfo:
  def __init__(self, cp: ConstantPool) -> None:
    self.__cp: ConstantPool = cp
    self.access_flags: uint16
    self.name_index: uint16
    self.descriptor_index: uint16
    self.attributes: list[AttributeInfo]

  def name(self) -> str:
    return self.__cp.get_utf8(self.name_index)

  def descriptor(self) -> str:
    return self.__cp.get_utf8(self.descriptor_index)

  def code_attribute(self) -> CodeAttributeInfo:
    for info in self.attributes:
      match info:
        case CodeAttributeInfo():
          return info

    return None
  def constant_value_attribute(self)-> ConstantValueAttributeInfo:
    for attr_info in self.attributes:
      match attr_info:
        case ConstantValueAttributeInfo():
          return attr_info 
    
    return None


def read_members(reader: ClassReader, cp: ConstantPool) -> list[MemberInfo]:
  counts = reader.read_u16()
  # members = [read_member(reader, cp) for i in range(counts)]
  members = []
  for i in range(counts):
    members.append(read_member(reader, cp))
  return members


def read_member(reader: ClassReader, cp: ConstantPool) -> MemberInfo:
  info = MemberInfo(cp)
  info.access_flags = reader.read_u16()
  info.name_index = reader.read_u16()
  info.descriptor_index = reader.read_u16()
  info.attributes = read_attributes(reader, cp)
  return info


def read_attribute(reader: ClassReader, cp: ConstantPool) -> AttributeInfo:
  attribute_name_index = reader.read_u16()
  code = cp.get_utf8(attribute_name_index)
  attribute_length = reader.read_u32()
  ai: AttributeInfo
  match code:
    case "Code":
      ai = CodeAttributeInfo(attribute_name_index, attribute_length, cp)
    case "LineNumberTable":
      ai = LineNumberTableAttrInfo(attribute_name_index, attribute_length, cp)
    case "SourceFile":
      ai = SourceFileAttributeInfo(attribute_name_index, attribute_length, cp)
    case "Deprecated":
      ai = DeprecatedAttributeInfo(attribute_name_index, attribute_length, cp)
    case "Synthetic":
      ai = SyntheticAttributeInfo(attribute_name_index, attribute_length, cp)
    case "ConstantValue":
      ai = ConstantValueAttributeInfo( attribute_name_index, attribute_length, cp)
    case "Exceptions":
      ai = ExceptionsAttributeInfo(attribute_name_index, attribute_length, cp)
    case _:
      ai = UnparsedAttributeInfo(attribute_name_index, attribute_length, cp)
  ai.read_info(reader)
  return ai


def read_attributes(reader: ClassReader, cp: ConstantPool) -> list[AttributeInfo]:
  counts = reader.read_u16()
  # attrs = [read_attribute(reader, cp) for i in range(counts)]
  attrs = []
  for i in range(counts):
    attrs.append(read_attribute(reader, cp))
  return attrs


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
    self.read_and_check_version(reader)

    self.constant_pool = read_constant_pool(reader)
    # print(f'constant pool = {self.constant_pool}')

    self.access_flags = reader.read_u16()
    self.this_class = reader.read_u16()
    self.super_class = reader.read_u16()
    self.interfaces = reader.read_u16s()
    self.fields = read_members(reader, self.constant_pool)
    self.methods = read_members(reader, self.constant_pool)
    self.attributes = read_attributes(reader, self.constant_pool)

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

    if self.major_version in [46, 47, 49, 50, 51, 52, 55] and self.minor_version == 0:
      return
    raise Err(
        f"Unsupport class file version: {self.minor_version=} {self.major_version}")

  def class_name(self, ) -> str:
      return self.constant_pool.get_class_name(self.this_class)
      # assert False, f'to be implemented'

  def super_class_name(self, ) -> str:
      if self.super_class > 0:
        return self.constant_pool.get_class_name(self.super_class)
      return ''
    # assert False, f'to be implemented'

  def interface_names(self) -> list[str]:
      return [self.constant_pool.get_class_name(inter) for inter in self.interfaces]
    # assert False, f'to be implemented'


def parse(class_data: bytes) -> tuple[ClassFile, Err]:
  try:
    cr = ClassReader(class_data)
    cf = ClassFile()
    cf.read(cr)
    if not cr.is_end():
      raise Exception("parse error: class file are not fully parsed.")
  except Exception as e:
    logging.error(f"could not read class file: {e}")
    return None, e

  return cf, None
