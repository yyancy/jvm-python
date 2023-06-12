from jvm.instructions.base.class_init_logic import init_class
from jvm.rtda.frame import *
from jvm.rtda.heap.object import Object
from jvm.rtda.heap.string_pool import jstring
from jvm.rtda.thread import Thread
from parse import *
import jvm.native
import jvm.rtda.heap.class_loader as loader
from jvm.classpath.new_entry import *
from jvm.classfile.class_file import *
import jvm.classpath.classpath as classpath
from objprint import op
import logging
import pprint
import interperter

logging.basicConfig(
    format="%(levelname)-2s [%(filename)s:%(lineno)d] %(message)s", level=logging.INFO
)


pp = pprint.PrettyPrinter(indent=4)
# logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
#                     datefmt='%Y-%m-%d:%H:%M:%S',
#                     level=logging.INFO)


def start_jvm(cmd: Cmd):
    cp = classpath.parse(cmd.XjreOption, cmd.cpOption)
    class_loader = loader.ClassLoader(cp, cmd.verboseClassFlag)
    logging.info(f"classpath: [{cp}] class: [{cmd.clazz}] args: [{cmd.args}]")
    class_name = cmd.clazz.replace(".", "/", -1)
    main_class = class_loader.load_class(class_name)
    main_method = main_class.get_main_method()
    # op(main_method)
    # class_data, _, err = cp.read_class(class_name)
    # if err != None:
    #   print(f"Could not find or load main class {cmd.clazz}: {err}")
    #   return
    # print(f"class data: {class_data}")
    # [cf, e] = parse(class_data)
    # if e != None:
    #   raise e

    # op(cf)

    # main_method = get_main_method(cf)
    if main_method != None:
        interperter.interpret(main_method, cmd.verboseInstFlag, cmd.args)
    else:
        logging.warning(f"Main method not found in class {cmd.clazz}")


class JVM:
    def __init__(self, cmd: Cmd) -> None:
        self.cmd = cmd
        cp = classpath.parse(cmd.XjreOption, cmd.cpOption)
        self.class_loader = loader.ClassLoader(cp, cmd.verboseClassFlag)
        self.main_thread = Thread()

    def create_args_array(self) -> Object:
        string_class = self.loader.load_class("java/lang/String")
        args_arr = string_class.array_class().new_array(len(self.cmd.args))
        jargs = args_arr.refs()
        for i in range(len(self.cmd.args)):
            jargs[i] = jstring(self.class_loader, self.cmd.args[i])
        return args_arr

    def start(self):
        self.init_vm()
        self.exec_main()

    def init_vm(self):
        vm_class = self.class_loader.load_class("sun/misc/VM")
        init_class(self.main_thread, vm_class)
        interperter.interpret(self.main_thread, self.cmd.verboseInstFlag)

    def exec_main(self):
        class_name = self.cmd.clazz.replace(".", "/", -1)
        main_class = self.class_loader.load_class(class_name)
        main_method = main_class.get_main_method()

        if main_method is None:
            logging.warning(f"Main method not found in class {cmd.clazz}")
            return
        logging.error(233)
        args_arr = self.create_args_array()
        frame = self.main_thread.new_frame(main_method)
        frame.local_vars.set_ref(0, args_arr)
        self.main_thread.push_frame(frame)

        interperter.interpret(self.main_thread, self.cmd.verboseInstFlag)


def get_main_method(cf: ClassFile) -> MemberInfo:
    return next(
        (
            method
            for method in cf.methods
            if method.name() == "main"
            and method.descriptor() == "([Ljava/lang/String;)V"
        ),
        None,
    )


if __name__ == "__main__":
    cmd = parse_cmd()
    # start_jvm(cmd)
    JVM(cmd).start()
