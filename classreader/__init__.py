

class ClassReader:
    def __init__(self) -> None:
        self.data
    
    def read_ubytes(self, count):
        return int.from_bytes(self.data.read(count),'big')

    def read_bytes(self, count):
        return self.data.read(count)
      

    def read_u8(self)-> int:
      return self.read_bytes(1)

    def read_u16(self)-> int:
      return self.read_bytes(2)

    def read_u32(self)-> int:
      return self.read_bytes(4)

    def read_u64(self)-> int:
      return self.read_bytes(8)