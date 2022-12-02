from .entry import *
from .entry_wildcard import *
from os.path import exists

class Classpath:
    def __init__(self) -> None:
        self.boot_classpath:Entry
        self.ext_classpath:Entry
        self.user_classpath:Entry

    def read_class(self,class_name: str) -> tuple[bytes, Entry, Err]:
        class_name = class_name+'.class'
        data, entry, err = self.boot_classpath.read_class(class_name)
        if err == None:
          return data, entry, err
        
        data, entry, err = self.ext_classpath.read_class(class_name)
        if err == None:
          return data, entry, err
        
        return self.user_classpath.read_class(class_name)
        
    def __str__(self) -> str:
      return str(self.user_classpath)

    def parse_boot_and_ext_classpath(self, jre_option:str)->None:
        jre_dir = get_jre_dir(jre_option)
        # jre/lib/*
        jre_lib_path = os.path.join(jre_dir,"lib","*")
        self.boot_classpath = new_wildcard_entry(jre_lib_path)
        # jre/lib/ext/*
        jre_ext_path =  os.path.join(jre_dir,"lib","ext","*")
        self.ext_classpath = new_wildcard_entry(jre_ext_path)


    def parse_user_classpath(self, cp_option:str)->None:
        if cp_option == "" or cp_option == None:
          cp_option = "."
        self.user_classpath = new_entry(cp_option)

def get_jre_dir(jre_option:str) -> str:
    if jre_option!="" and exists(jre_option):
        return jre_option

    cur = os.path.join(',','jre')
    if exists(cur):
        return cur

    jh = os.environ['JAVA_HOME']
    if jh != "":
      return os.path.join(jh, 'jre')
    
    assert False, "Can not find jre folder!"



def parse(jre_option, cp_option: str) -> Classpath:
    cp = Classpath()
    cp.parse_boot_and_ext_classpath(jre_option)
    cp.parse_user_classpath(cp_option)
    return cp
