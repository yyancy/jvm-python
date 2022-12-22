import io


class BytecodeReader:
  def __init__(self) -> None:
    self.code: io.bytesIO
    self.pc: int = 0

  def reset(self, code: bytes, pc: int) -> None:
    self.code: io.BytesIO = io.BytesIO(code)
    self.pc: int = pc

  def read_ubytes(self, count) -> int:
    i = int.from_bytes(self.data.read(count), 'big')
    self.pc += count
    return i

  def read_bytes(self, count) -> bytes:
    i = self.data.read(count)
    self.pc += count
    return i

  def read_u8(self) -> int:
    return self.read_ubytes(1)

  def read_u16(self) -> int:
    return self.read_ubytes(2)

  def read_u32(self) -> int:
    return self.read_ubytes(4)

  def read_u64(self) -> int:
    return self.read_ubytes(8)

  def is_end(self) -> bool:
    return self.data.tell() >= self.len

  def skip_padding(self):
    while self.pc % 4 != 0:
      self.read_u8()

  def read_u32s(self, count: int) -> list[int]:
    # s = []
    # for i in range(count):
    #   s.append(self.read_u32())
    # return s
    return [self.read_u32() for _ in range(count)]

  def is_end(self) -> bool:
    return self.data.tell() >= self.len
