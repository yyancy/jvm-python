from .entry import Entry
from .entry import Err
import zipfile
import os.path
import logging

class ZipEntry(Entry):
  def __init__(self, path:str) -> None:
     super().__init__()
     self.abs_path = path
     
     
  def read_class(self, class_name: str) -> tuple[bytes,Entry, Err]:
    zip = zipfile.ZipFile(self.abs_path)
    logging.info(f"{self.abs_path=}")
    for file in zip.namelist():
      if file == class_name:
        with zip.open(class_name) as f:
          b = f.read()
          return b, self, None
    return None, None, Err(f"class not found: {class_name}")


  def __str__(self) -> str:
    return self.abs_path


def new_zip_entry(path: str)-> ZipEntry:
  path = os.path.abspath(path)
  return ZipEntry(path)