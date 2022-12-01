from parse import *
from classpath.new_entry import *

def start_jvm(cmd: Cmd):
    print(f"{cmd=}")
    e = new_entry('/admin:yancy:666')
    print(e)
    e.read_class('demo')


if __name__ == '__main__':
    cmd = parse_cmd()
    start_jvm(cmd)
