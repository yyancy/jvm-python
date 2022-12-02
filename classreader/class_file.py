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


class ConstantPool:
  pass


class MemberInfo:
  def __init__(self) -> None:
    self.cp: ConstantPool
    self.access_flags: uint16
    self.name_index: uint16
    self.descriptor_index: uint16
    self.attributes: list[AttributeInfo]
  pass


def read_constant_pool(reader: ClassReader) -> ConstantPool:
  pass


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
    magic = reader.read_u32()
    if magic != 0xCAFEBABE:
      raise Err(
          f"java.lang.ClassFormatError: expected magic number 0xCAFEBABE, got {magic:0x}")
    self.magic = magic

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
