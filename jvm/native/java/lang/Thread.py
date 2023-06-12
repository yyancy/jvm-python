

#  public static native Thread currentThread();
#  ()Ljava/lang/Thread;
from jvm.rtda.frame import Frame


def currentThread(frame: Frame):
  # jThread = frame.Thread().JThread()
  classLoader = frame.method.clazz.loader
  threadClass = classLoader.load_class("java/lang/Thread")
  jThread = threadClass.new_object()

  threadGroupClass = classLoader.load_class("java/lang/ThreadGroup")
  jGroup = threadGroupClass.new_object()

  jThread.set_refvar("group", "Ljava/lang/ThreadGroup;", jGroup)
  jThread.set_intvar("priority", "I", 1)

  frame.operand_stack.push_ref(jThread)


#  private native void setPriority0(int newPriority);
#  (I)V
def setPriority0(frame: Frame):
  #  vars = frame.LocalVars()
  #  this = vars.GetThis()
  #  newPriority = vars.GetInt(1))
  #  todo
  pass


#  public final native boolean isAlive();
#  ()Z

def isAlive(frame: Frame):
  # vars = frame.LocalVars()
  # this = vars.GetThis()

  stack = frame.operand_stack
  stack.push_bool(False)


#  private native void start0();
#  ()V
def start0(frame: Frame):
  #  todo
  pass
