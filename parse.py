import argparse
from dataclasses import dataclass


@dataclass
class Cmd:
  cpOption: str
  clazz: str
  XjreOption: str
  verboseClassFlag: bool
  verboseInstFlag: bool
  args: list


def show_version():
  return "0.1 version"


def parse_cmd() -> Cmd:
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--version", help="show version",
                      action="version", version=show_version())
  parser.add_argument("-c", "--classpath", help="classpath",
                      type=str, action="store", dest="classpath")
  parser.add_argument("-jre", "--Xjre", help="path to jre",
                      type=str, action="store", dest="Xjre")
  parser.add_argument("clazz", help="class file name",
                      type=str, action="store")
  parser.add_argument("--verbose:inst", help="print logs of instruction",
                      type=bool, action=argparse.BooleanOptionalAction, dest='instFlag')
  parser.add_argument("--verbose:class", help="print class of instruction",
                      type=bool, action="store", dest='classFlag')
  args, unknown = parser.parse_known_args()
  cmd = Cmd(args.classpath, args.clazz, args.Xjre,
            args.classFlag, args.instFlag, unknown)
  return cmd
