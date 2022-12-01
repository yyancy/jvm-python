import argparse
from dataclasses import dataclass

@dataclass
class Cmd:
    cpOption: str
    clazz: str
    XjreOption: str
    args: list

def show_version():
    return "0.1 version"


def parse_cmd() -> Cmd:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", help="show version",
                        action="version",version=show_version())
    parser.add_argument("-c","--classpath", help="classpath",
                        type=str, action="store", dest="classpath")
    parser.add_argument("-jre","--Xjre", help="path to jre",
                        type=str, action="store", dest="Xjre")
    parser.add_argument("clazz", help="class file name",
                        type=str, action="store")
    args, unknown = parser.parse_known_args()
    cmd = Cmd(args.classpath, args.clazz,args.Xjre, unknown)
    return cmd
