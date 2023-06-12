
from jvm.rtda.frame import Frame
from jvm.instructions.base.method_invoke_logic import invoke_method


#  @CallerSensitive
#  public static native <T> T
#      doPrivileged(PrivilegedExceptionAction<T> action)
#      throws PrivilegedActionException;
#  (Ljava/security/PrivilegedExceptionAction;)Ljava/lang/Object;

#  @CallerSensitive
#  public static native <T> T doPrivileged(PrivilegedAction<T> action);
#  (Ljava/security/PrivilegedAction;)Ljava/lang/Object;
def doPrivileged(frame: Frame):
  _vars = frame.local_vars
  action = _vars.get_ref(0)

  stack = frame.operand_stack
  stack.push_ref(action)

  method = action.clazz.get_instance_method(
      "run", "()Ljava/lang/Object;")  # todo
  invoke_method(frame, method)

#  private static native AccessControlContext getStackAccessControlContext();
#  ()Ljava/security/AccessControlContext;


def getStackAccessControlContext(frame: Frame):
  #  todo
  frame.operand_stack.push_ref(None)
