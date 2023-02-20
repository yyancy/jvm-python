import os
from .entry_zip import *
from .entry_composite import *
def new_wildcard_entry(path:str):
    base_dir = path[:-1]
    composite_entry = CompositeEntry()
    for file in os.listdir(base_dir):
        if file.endswith(('.jar','.JAR')):
            jar_entry = new_zip_entry(os.path.join(base_dir,file))
            composite_entry.append(jar_entry)
  
    return composite_entry