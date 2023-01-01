from ..base.instruction import *

from common.cons import *
from rtda.frame import Frame


class WIDE(Instruction):
  def fetch_operands(self, reader: BytecodeReader):
    opcode = reader.read_u8()
    match opcode:
      case 0x15: # iload
        pass
      case 0x16: # iload
        pass
      case 0x17: # iload
        pass
      case 0x18: # iload
        pass
      case 0x19: # iload
        pass
      case 0x36: # iload
        pass
      case 0x37: # iload
        pass
      case 0x38: # iload
        pass
      case 0x39: # iload
        pass
      case 0x3a: # iload
        pass
      case 0x84: # iload
        pass
      case 0xa9: # iload
          assert False, f'0xa9 to be implemented'