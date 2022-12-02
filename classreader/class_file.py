from typing import NewType
from classpath.entry import Err

uint8 = NewType('uint8', int)
uint16 = NewType('uint16', int)
uint32 = NewType('uint32', int)
uint64 = NewType('uint64', int)

class AttributeInfo:
    pass

class ConstantPool:
    pass

class MemberInfo:
    pass
class ClassFile:
    def __init__(self) -> None:
        self.magic: uint32
        self.minor_version:uint16
        self.major_version:uint16
        self.constant_pool: ConstantPool
        self.access_flags: uint16
        self.this_class: uint16
        self.super_class: uint16
        self.interfaces: list[uint16]
        self.fields: list[MemberInfo]
        self.methods: list[MemberInfo]
        self.attributes: list[AttributeInfo]
        


      


def parse(class_data: bytes) -> tuple[ClassFile, Err]:
    pass