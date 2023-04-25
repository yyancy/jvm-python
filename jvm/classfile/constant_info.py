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


def utf8s_to_utf8m(string):
    """
    :param string: utf8 encoded string 
    :return: modified utf8 encoded string
    """
    new_str = []
    i = 0
    while i < len(string):
        byte1 = string[i]
        # NULL bytes and bytes starting with 11110xxx are special
        if (byte1 & 0x80) == 0:
            if byte1 == 0:
                new_str.append(0xC0)
                new_str.append(0x80)
            else:
                # Single byte
                new_str.append(byte1)

        elif (byte1 & 0xE0) == 0xC0:  # 2byte encoding
            new_str.append(byte1)
            i += 1
            new_str.append(string[i])

        elif (byte1 & 0xF0) == 0xE0:  # 3byte encoding
            new_str.append(byte1)
            i += 1
            new_str.append(string[i])
            i += 1
            new_str.append(string[i])

        elif (byte1 & 0xF8) == 0xF0:  # 4byte encoding
            # Beginning of 4byte encoding, turn into 2 3byte encodings
            # Bits in: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
            i += 1
            byte2 = string[i]
            i += 1
            byte3 = string[i]
            i += 1
            byte4 = string[i]

            # Reconstruct full 21bit value
            u21 = (byte1 & 0x07) << 18
            u21 += (byte2 & 0x3F) << 12
            u21 += (byte3 & 0x3F) << 6
            u21 += (byte4 & 0x3F)

            # Bits out: 11101101 1010xxxx 10xxxxxx
            new_str.append(0xED)
            new_str.append((0xA0 + (((u21 >> 16) - 1) & 0x0F)))
            new_str.append((0x80 + ((u21 >> 10) & 0x3F)))

            # Bits out: 11101101 1011xxxx 10xxxxxx
            new_str.append(0xED)
            new_str.append((0xB0 + ((u21 >> 6) & 0x0F)))
            new_str.append(byte4)
        i += 1
    return bytes(new_str)


def utf8m_to_utf8s(string):
    """
    :param string: modified utf8 encoded string 
    :return: utf8 encoded string
    """
    new_string = []
    length = len(string)
    i = 0
    while i < length:
        byte1 = string[i]
        if (byte1 & 0x80) == 0:  # 1byte encoding
            new_string.append(byte1)
        elif (byte1 & 0xE0) == 0xC0:  # 2byte encoding
            i += 1
            byte2 = string[i]
            if byte1 != 0xC0 or byte2 != 0x80:
                new_string.append(byte1)
                new_string.append(byte2)
            else:
                new_string.append(0)
        elif (byte1 & 0xF0) == 0xE0:  # 3byte encoding
            i += 1
            byte2 = string[i]
            i += 1
            byte3 = string[i]
            if i+3 < length and byte1 == 0xED and (byte2 & 0xF0) == 0xA0:
                # See if this is a pair of 3byte encodings
                byte4 = string[i+1]
                byte5 = string[i+2]
                byte6 = string[i+3]
                if byte4 == 0xED and (byte5 & 0xF0) == 0xB0:
                    
                    # Bits in: 11101101 1010xxxx 10xxxxxx
                    # Bits in: 11101101 1011xxxx 10xxxxxx
                    i += 3
                    
                    # Reconstruct 21 bit code
                    u21 = ((byte2 & 0x0F) + 1) << 16
                    u21 += (byte3 & 0x3F) << 10
                    u21 += (byte5 & 0x0F) << 6
                    u21 += (byte6 & 0x3F)
                    
                    # Bits out: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
                    
                    # Convert to 4byte encoding
                    new_string.append(0xF0 + ((u21 >> 18) & 0x07))
                    new_string.append(0x80 + ((u21 >> 12) & 0x3F))
                    new_string.append(0x80 + ((u21 >> 6) & 0x3F))
                    new_string.append(0x80 + (u21 & 0x3F))
                    continue 
            new_string.append(byte1)
            new_string.append(byte2)
            new_string.append(byte3)
        i += 1
    return bytes(new_string)


class Utf8ConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.length: uint16
    self.value: str

  def read_info(self, reader: ClassReader) -> None:
    self.length = reader.read_u16()
    data = reader.read_bytes(self.length)
    # self.value = data.decode('utf-8')
    self.value = utf8m_to_utf8s(data).decode('utf-8')


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
    [self.value] = struct.unpack('>d', data)


class FloatConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.value: float

  def read_info(self, reader: ClassReader) -> None:
    import struct
    data = reader.read_bytes(4)
    [self.value] = struct.unpack('>f', data)


class LongConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.value: int

  def read_info(self, reader: ClassReader) -> None:
    b = reader.read_bytes(8)
    self.value = int.from_bytes(b, 'big', signed=True)


class IntegerConstantInfo(ConstantInfo):
  def __init__(self, tag: int, cp: ConstantPool) -> None:
    super().__init__(tag, cp)
    self.value: int

  def read_info(self, reader: ClassReader) -> None:
    b = reader.read_bytes(4)
    self.value = int.from_bytes(b, 'big', signed=True)


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