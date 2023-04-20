from __future__ import annotations
from .constant_pool import *
from .class_reader import *
from jvm.common.cons import *

# from .constant_pool import ConstantPool


class ConstantInfo:
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    self.tag = tag
    self.__cp = cp

  def read_info(self, reader: ClassReader) -> None:
    raise Exception("not implemented!")

  def __repr__(self) -> str:
    s=vars(self)
    return str(s)
  
  def cp(self)-> ConstantPool:
    return self.__cp


class InvokeDynamicConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.bootstrap_method_attr_index: uint16
    self.name_and_type_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.bootstrap_method_attr_index = reader.read_u16()
    self.name_and_type_index = reader.read_u16()


class MethodTypeConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.descriptor_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.descriptor_index = reader.read_u16()


class MethodHandleConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.reference_kind: uint8
    self.reference_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.reference_kind = reader.read_u8()
    self.reference_index = reader.read_u16()


class Utf8ConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.length: uint16
    self.value: str

  def read_info(self, reader: ClassReader) -> None:
    self.length = reader.read_u16()
    data = reader.read_bytes(self.length)
    self.value = data.decode('utf-8')


class NameAndTypeConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.name_index: uint16
    self.descriptor_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.name_index = reader.read_u16()
    self.descriptor_index = reader.read_u16()


class DoubleConstantInfo(ConstantInfo):
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
  
  def string(self)-> str:
    return self.cp().get_utf8(self.string_index)



class MemberrefConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.class_index: uint16
    self.name_and_type_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.class_index = reader.read_u16()
    self.name_and_type_index = reader.read_u16()
  
  def class_name(self)-> str:
    return self.cp().get_class_name(self.class_index)
  
  def name_and_descriptor(self)-> tuple[str, str]:
    return self.cp().get_name_and_type(self.name_and_type_index)
  



class InterfaceMethodrefConstantInfo(MemberrefConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    # self.info: ConstantInfo = CommonConstantInfo(tag, cp)


class MethodrefConstantInfo(MemberrefConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
  
  def __str__(self) -> str:
    return str(self.info)


class FieldrefConstantInfo(MemberrefConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)


class ClassConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.name_index: uint16

  def read_info(self, reader: ClassReader) -> None:
    self.name_index = reader.read_u16()
  
  def name(self)->str:
    return self.cp().get_utf8(self.name_index)