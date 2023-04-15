
from jvm.rtda.frame import Frame
from jvm.instructions.base.instruction import NoOperandsInstuction
from jvm.native import registry

class INVOKE_NATIVE(NoOperandsInstuction):
  def execute(self, frame: Frame):
    method = frame.method
    class_name = method.clazz.name
    method_name = method.name
    method_descriptor = method.descriptor
    native_method = registry.find_native_method(class_name,
                                              method_name,
                                              method_descriptor)
    if native_method == None:
      method_info = f'{class_name}.{method_name}{method_descriptor}'
      raise SystemExit(f'java.lang.UnsatisfiedLinkError: {method_info}')

    native_method(frame)
