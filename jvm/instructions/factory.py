from jvm.instructions.control.mreturn import ARETURN, DRETURN, FRETURN, IRETURN, LRETURN, RETURN
from jvm.instructions.references.invokeinterface import INVOKE_INTERFACE
from jvm.instructions.references.invokestatic import INVOKE_STATIC
from jvm.instructions.stack.pop import POP, POP2
from jvm.instructions.stack.dup import DUP,DUP2, DUP2_X1,DUP2_X2,DUP_X1,DUP_X2
from jvm.instructions.stack.swap import SWAP
from . import *
from .base import *
from .comparisons import *
from .constants import *
from .loads import *
from .stores import *
from .maths import *
from .conversions import *
from .control import *
from .extended import *
from .references import *
import types

single = types.SimpleNamespace()
single.nop         = NOP()
single.aconst_null = ACONST_NULL()
single.iconst_m1   = ICONST_M1()
single.iconst_0    = ICONST_0()
single.iconst_1    = ICONST_1()
single.iconst_2    = ICONST_2()
single.iconst_3    = ICONST_3()
single.iconst_4    = ICONST_4()
single.iconst_5    = ICONST_5()
single.lconst_0    = LCONST_0()
single.lconst_1    = LCONST_1()
single.fconst_0    = FCONST_0()
single.fconst_1    = FCONST_1()
single.fconst_2    = FCONST_2()
single.dconst_0    = DCONST_0()
single.dconst_1    = DCONST_1()
single.iload_0     = ILOAD_0()
single.iload_1     = ILOAD_1()
single.iload_2     = ILOAD_2()
single.iload_3     = ILOAD_3()
single.lload_0     = LLOAD_0()
single.lload_1     = LLOAD_1()
single.lload_2     = LLOAD_2()
single.lload_3     = LLOAD_3()
single.fload_0     = FLOAD_0()
single.fload_1     = FLOAD_1()
single.fload_2     = FLOAD_2()
single.fload_3     = FLOAD_3()
single.dload_0     = DLOAD_0()
single.dload_1     = DLOAD_1()
single.dload_2     = DLOAD_2()
single.dload_3     = DLOAD_3()
single.aload_0     = ALOAD_0()
single.aload_1     = ALOAD_1()
single.aload_2     = ALOAD_2()
single.aload_3     = ALOAD_3()
# single.iaload      = IALOAD()
# single.laload      = LALOAD()
# single.faload      = FALOAD()
# single.daload      = DALOAD()
# single.aaload      = AALOAD()
# single.baload      = BALOAD()
# single.caload      = CALOAD()
# single.saload      = SALOAD()
single.istore_0 = ISTORE_0()
single.istore_1 = ISTORE_1()
single.istore_2 = ISTORE_2()
single.istore_3 = ISTORE_3()
single.lstore_0 = LSTORE_0()
single.lstore_1 = LSTORE_1()
single.lstore_2 = LSTORE_2()
single.lstore_3 = LSTORE_3()
single.fstore_0 = FSTORE_0()
single.fstore_1 = FSTORE_1()
single.fstore_2 = FSTORE_2()
single.fstore_3 = FSTORE_3()
single.dstore_0 = DSTORE_0()
single.dstore_1 = DSTORE_1()
single.dstore_2 = DSTORE_2()
single.dstore_3 = DSTORE_3()
single.astore_0 = ASTORE_0()
single.astore_1 = ASTORE_1()
single.astore_2 = ASTORE_2()
single.astore_3 = ASTORE_3()
# single.iastore  = IASTORE()
# single.lastore  = LASTORE()
# single.fastore  = FASTORE()
# single.dastore  = DASTORE()
# single.aastore  = AASTORE()
# single.bastore  = BASTORE()
# single.castore  = CASTORE()
# single.sastore  = SASTORE()
single.pop     = POP()
single.pop2    = POP2()
single.dup     = DUP()
single.dup_x1  = DUP_X1()
single.dup_x2  = DUP_X2()
single.dup2    = DUP2()
single.dup2_x1 = DUP2_X1()
single.dup2_x2 = DUP2_X2()
single.swap    = SWAP()
single.iadd    = IADD()
single.ladd    = LADD()
single.fadd    = FADD()
single.dadd    = DADD()
single.isub    = ISUB()
single.lsub    = LSUB()
single.fsub    = FSUB()
single.dsub    = DSUB()
single.imul    = IMUL()
single.lmul    = LMUL()
single.fmul    = FMUL()
single.dmul    = DMUL()
single.idiv    = IDIV()
single.ldiv    = LDIV()
single.fdiv    = FDIV()
single.ddiv    = DDIV()
single.irem    = IREM()
single.lrem    = LREM()
single.frem    = FREM()
single.drem    = DREM()
single.ineg    = INEG()
single.lneg    = LNEG()
single.fneg    = FNEG()
single.dneg    = DNEG()
single.ishl    = ISHL()
single.lshl    = LSHL()
single.ishr    = ISHR()
single.lshr    = LSHR()
single.iushr   = IUSHR()
single.lushr   = LUSHR()
single.iand    = IAND()
single.land    = LAND()
single.ior     = IOR()
single.lor     = LOR()
single.ixor    = IXOR()
single.lxor    = LXOR()
single.i2l     = I2L()
single.i2f     = I2F()
single.i2d     = I2D()
single.l2i     = L2I()
single.l2f     = L2F()
single.l2d     = L2D()
single.f2i     = F2I()
single.f2l     = F2L()
single.f2d     = F2D()
single.d2i     = D2I()
single.d2l     = D2L()
single.d2f     = D2F()
single.i2b     = I2B()
single.i2c     = I2C()
single.i2s     = I2S()
single.lcmp    = LCMP()
single.fcmpl   = FCMPL()
single.fcmpg   = FCMPG()
single.dcmpl   = DCMPL()
single.dcmpg   = DCMPG()
single.ireturn = IRETURN()
single.lreturn = LRETURN()
single.freturn = FRETURN()
single.dreturn = DRETURN()
single.areturn = ARETURN()
single._return = RETURN()
# single.arraylength   = ARRAY_LENGTH()
# single.athrow        = ATHROW()
# single.monitorenter  = MONITOR_ENTER()
# single.monitorexit   = MONITOR_EXIT()
# single.invoke_native = INVOKE_NATIVE()

    
def new_instruction(opcode :int) ->Instruction:
  match opcode:
    case 0x00:
      return single.nop
    case 0x01:
      return single.aconst_null
    case 0x02:
       return single.iconst_m1
    case 0x03:
      return single.iconst_0
    case 0x04:
      return single.iconst_1
    case 0x05:
      return single.iconst_2
    case 0x06:
      return single.iconst_3
    case 0x07:
      return single.iconst_4
    case 0x08:
      return single.iconst_5
    case 0x09:
      return single.lconst_0
    case 0x0a:
      return single.lconst_1
    case 0x0b:
      return single.fconst_0
    case 0x0c:
      return single.fconst_1
    case 0x0d:
      return single.fconst_2
    case 0x0e:
      return single.dconst_0
    case 0x0f:
        return single.dconst_1
    case 0x10:
      return BIPUSH()
    case 0x11:
      return SIPUSH()
    case 0x12:
       return LDC()
    case 0x13:
       return LDC_W()
    case 0x14:
       return LDC2_W()
    case 0x15:
      return ILOAD()
    case 0x16:
      return LLOAD()
    case 0x17:
      return FLOAD()
    case 0x18:
      return DLOAD()
    case 0x19:
      return ALOAD()
    case 0x1a:
      return single.iload_0
    case 0x1b:
      return single.iload_1
    case 0x1c:
      return single.iload_2
    case 0x1d:
      return single.iload_3
    case 0x1e:
      return single.lload_0
    case 0x1f:
      return single.lload_1
    case 0x20:
      return single.lload_2
    case 0x21:
      return single.lload_3
    case 0x22:
      return single.fload_0
    case 0x23:
      return single.fload_1
    case 0x24:
      return single.fload_2
    case 0x25:
      return single.fload_3
    case 0x26:
      return single.dload_0
    case 0x27:
      return single.dload_1
    case 0x28:
      return single.dload_2
    case 0x29:
      return single.dload_3
    case 0x2a:
      return single.aload_0
    case 0x2b:
      return single.aload_1
    case 0x2c:
      return single.aload_2
    case 0x2d:
      return single.aload_3
    # case 0x2e:
    # 	return iaload
    # case 0x2f:
    # 	return laload
    # case 0x30:
    # 	return faload
    # case 0x31:
    # 	return daload
    # case 0x32:
    # 	return aaload
    # case 0x33:
    # 	return baload
    # case 0x34:
    # 	return caload
    # case 0x35:
    # 	return saload
    case 0x36:
      return ISTORE()
    case 0x37:
      return LSTORE()
    case 0x38:
      return FSTORE()
    case 0x39:
      return DSTORE()
    case 0x3a:
      return ASTORE()
    case 0x3b:
      return single.istore_0
    case 0x3c:
      return single.istore_1
    case 0x3d:
      return single.istore_2
    case 0x3e:
      return single.istore_3
    case 0x3f:
      return single.lstore_0
    case 0x40:
      return single.lstore_1
    case 0x41:
      return single.lstore_2
    case 0x42:
      return single.lstore_3
    case 0x43:
      return single.fstore_0
    case 0x44:
      return single.fstore_1
    case 0x45:
      return single.fstore_2
    case 0x46:
      return single.fstore_3
    case 0x47:
      return single.dstore_0
    case 0x48:
      return single.dstore_1
    case 0x49:
      return single.dstore_2
    case 0x4a:
      return single.dstore_3
    case 0x4b:
      return single.astore_0
    case 0x4c:
      return single.astore_1
    case 0x4d:
      return single.astore_2
    case 0x4e:
      return single.astore_3
    # case 0x4f:
    # 	return iastore
    # case 0x50:
    # 	return lastore
    # case 0x51:
    # 	return fastore
    # case 0x52:
    # 	return dastore
    # case 0x53:
    # 	return aastore
    # case 0x54:
    # 	return bastore
    # case 0x55:
    # 	return castore
    # case 0x56:
    # 	return sastore
    case 0x57:
      return single.pop
    case 0x58:
      return single.pop2
    case 0x59:
      return single.dup
    case 0x5a:
      return single.dup_x1
    case 0x5b:
      return single.dup_x2
    case 0x5c:
      return single.dup2
    case 0x5d:
      return single.dup2_x1
    case 0x5e:
      return single.dup2_x2
    case 0x5f:
      return single.swap
    case 0x60:
      return single.iadd
    case 0x61:
      return single.ladd
    case 0x62:
      return single.fadd
    case 0x63:
      return single.dadd
    case 0x64:
      return single.isub
    case 0x65:
      return single.lsub
    case 0x66:
      return single.fsub
    case 0x67:
      return single.dsub
    case 0x68:
      return single.imul
    case 0x69:
      return single.lmul
    case 0x6a:
      return single.fmul
    case 0x6b:
      return single.dmul
    case 0x6c:
      return single.idiv
    case 0x6d:
      return single.ldiv
    case 0x6e:
      return single.fdiv
    case 0x6f:
      return single.ddiv
    case 0x70:
      return single.irem
    case 0x71:
      return single.lrem
    case 0x72:
      return single.frem
    case 0x73:
      return single.drem
    case 0x74:
      return single.ineg
    case 0x75:
      return single.lneg
    case 0x76:
      return single.fneg
    case 0x77:
      return single.dneg
    case 0x78:
      return single.ishl
    case 0x79:
      return single.lshl
    case 0x7a:
      return single.ishr
    case 0x7b:
      return single.lshr
    case 0x7c:
      return single.iushr
    case 0x7d:
      return single.lushr
    case 0x7e:
      return single.iand
    case 0x7f:
      return single.land
    case 0x80:
      return single.ior
    case 0x81:
      return single.lor
    case 0x82:
      return single.ixor
    case 0x83:
      return single.lxor
    case 0x84:
      return IINC()
    case 0x85:
      return single.i2l
    case 0x86:
      return single.i2f
    case 0x87:
      return single.i2d
    case 0x88:
      return single.l2i
    case 0x89:
      return single.l2f
    case 0x8a:
      return single.l2d
    case 0x8b:
      return single.f2i
    case 0x8c:
      return single.f2l
    case 0x8d:
      return single.f2d
    case 0x8e:
      return single.d2i
    case 0x8f:
      return single.d2l
    case 0x90:
      return single.d2f
    case 0x91:
      return single.i2b
    case 0x92:
      return single.i2c
    case 0x93:
      return single.i2s
    case 0x94:
      return single.lcmp
    case 0x95:
      return single.fcmpl
    case 0x96:
      return single.fcmpg
    case 0x97:
      return single.dcmpl
    case 0x98:
      return single.dcmpg
    case 0x99:
      return IFEQ()
    case 0x9a:
      return IFNE()
    case 0x9b:
      return IFLT()
    case 0x9c:
      return IFGE()
    case 0x9d:
      return IFGT()
    case 0x9e:
      return IFLE()
    case 0x9f:
      return IF_ICMPEQ()
    case 0xa0:
      return IF_ICMPNE()
    case 0xa1:
      return IF_ICMPLT()
    case 0xa2:
      return IF_ICMPGE()
    case 0xa3:
      return IF_ICMPGT()
    case 0xa4:
      return IF_ICMPLE()
    case 0xa5:
      return IF_ACMPEQ()
    case 0xa6:
      return IF_ACMPNE()
    case 0xa7:
      return GOTO()
    # case 0xa8:
    # 	return &JSR{}
    # case 0xa9:
    # 	return &RET{}
    case 0xaa:
      return TABLE_SWITCH()
    case 0xab:
      return LOOKUP_SWITCH()
    case 0xac:
      return single.ireturn
    case 0xad:
      return single.lreturn
    case 0xae:
      return single.freturn
    case 0xaf:
      return single.dreturn
    case 0xb0:
      return single.areturn
    case 0xb1:
      return single._return
    case 0xb2:
      return GET_STATIC()
    case 0xb3:
      return PUT_STATIC()
    case 0xb4:
      return GET_FIELD()
    case 0xb5:
      return PUT_FIELD()
    case 0xb6:
       return INVOKE_VIRTUAL()
    case 0xb7:
       return INVOKE_SPECIAL()
    case 0xb8:
      return INVOKE_STATIC()
    case 0xb9:
      return INVOKE_INTERFACE()
    # case 0xba:
    # 	return &INVOKE_DYNAMIC{}
    case 0xbb:
       return NEW()
    # case 0xbc:
    # 	return &NEW_ARRAY{}
    # case 0xbd:
    # 	return &ANEW_ARRAY{}
    # case 0xbe:
    # 	return arraylength
    # case 0xbf:
    # 	return athrow
    case 0xc0:
       return CHECK_CAST()
    case 0xc1:
       return INSTANCE_OF()
    # case 0xc2:
    # 	return monitorenter
    # case 0xc3:
    # 	return monitorexit
    case 0xc4:
      return WIDE()
    # case 0xc5:
    # 	return &MULTI_ANEW_ARRAY{}
    case 0xc6:
      return IFNULL()
    case 0xc7:
      return IFNONNULL()
    case 0xc8:
      return GOTO_W()
    # case 0xc9:
    # 	return &JSR_W{}
    # case 0xca: breakpoint
    # case 0xfe: impdep1
    # case 0xff: impdep2
    case _:
      assert False, f'Unsupported opcode: {opcode:x}'
