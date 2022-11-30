from parse import *

def start_jvm(cmd: Cmd):
    print(f"{cmd=}")

if __name__ == '__main__':
    cmd = parse_cmd()
    start_jvm(cmd)
