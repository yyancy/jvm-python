
import io
from io import BufferedReader


class ClassReader:
  def __init__(self, data: bytes) -> None:
    self.len = len(data)
    self.data = io.BytesIO(data)

  def read_ubytes(self, count) -> int:
    return int.from_bytes(self.data.read(count), 'big')

  def read_bytes(self, count) -> bytes:
    return self.data.read(count)

  def read_u8(self) -> int:
    return self.read_ubytes(1)

  def read_u16(self) -> int:
    return self.read_ubytes(2)

  def read_u16s(self) -> list[int]:
    n = self.read_u16()
    s = []
    for i in range(n):
      s.append(self.read_u16())
    return s
  def is_end(self)->bool:
    return self.data.tell() >= self.len

  def read_u32(self) -> int:
    return self.read_ubytes(4)

  def read_u64(self) -> int:
    return self.read_ubytes(8)
  
  def read_sbytes(self, count) -> int:
    return int.from_bytes(self.data.read(count), 'big', signed=True)
  
  def read_s32(self)-> int:
    return self.read_sbytes(4)

