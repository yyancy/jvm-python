
class ClassReader:
    def __init__(self, data:bytes) -> None:
        self.data = data
    
    def read_ubytes(self, count):
        return int.from_bytes(self.data.read(count),'big')

    def read_bytes(self, count):
        return self.data.read(count)
      

    def read_u8(self)-> int:
      return self.read_bytes(1)

    def read_u16(self)-> int:
      return self.read_bytes(2)

    def read_u16s(self)-> list[int]:
        n = self.read_u16()
        s = []
        for i in range(n):
          s[i] = self.read_u16()
        return s

    def read_u32(self)-> int:
      return self.read_bytes(4)

    def read_u64(self)-> int:
      return self.read_bytes(8)