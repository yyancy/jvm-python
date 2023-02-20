from .entry import Entry
from .entry import Err
import zipfile
import os.path
from .new_entry import new_entry

class CompositeEntry(Entry):
  def __init__(self) -> None:
     super().__init__()
     self.entries:list[Entry] = []
     
     
  def read_class(self, class_name: str) -> tuple[bytes,Entry, Err]:
    for entry in self.entries:
      b, read_entry, e = entry.read_class(class_name)
      if e == None:
        return b, read_entry, None
    
    return 0, 0, Err(f"cannot find this class: {class_name}")
    # print(f"{self.entries=}")

  def append(self, e:Entry)-> None:
    self.entries.append(e)

  def __str__(self) -> str:
    s = ""
    for entry in self.entries:
      s += str(entry)
    return s


def new_composite_entry(path_list: str)-> CompositeEntry:
  entry = CompositeEntry()
  for path in path_list.split(os.path.pathsep):
    entry.append(new_entry(path))
  return entry