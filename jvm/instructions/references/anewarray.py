



from jvm.instructions.base.instruction import Index16Instuction
from jvm.rtda.frame import Frame
from jvm.rtda.heap.cp_classref import ClassRef


class ANEW_ARRAY(Index16Instuction):
    def execute(self, frame: Frame):
      cp = frame.method.clazz.constant_pool
      class_ref: ClassRef = cp.get_constant(self.index)
      component_class = class_ref.resolved_class()
      stack = frame.operand_stack
      count = stack.pop_int()
      if count < 0:
        raise SystemExit(f'java.lang.NegativeArraySizeException')
      
      arr_class = component_class.array_class()
      arr = arr_class.new_array(count)
      stack.push_ref(arr)
         

