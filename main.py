# constant pool enum
CONSTANT_CLASS               =   7
CONSTANT_FIELDREF            =   9
CONSTANT_METHODREF           =   10
CONSTANT_INTERFACE_METHODREF =   11
CONSTANT_STRING              =   8
CONSTANT_INTEGER             =   3
CONSTANT_FLOAT               =   4
CONSTANT_LONG                =   5
CONSTANT_DOUBLE              =   6
CONSTANT_NAME_AND_TYPE       =   12
CONSTANT_UTF8                =   1
CONSTANT_METHOD_HANDLE       =   15
CONSTANT_METHOD_TYPE         =   16
CONSTANT_INVOKE_DYNAMIC      =   18
def read_ubytes(f, count):
    return int.from_bytes(f.read(count),'big')


def read_u1(f):
    return read_ubytes(f, 1)

def read_u2(f):
    return read_ubytes(f, 2)
def read_u4(f):
    return read_ubytes(f, 4)
def read_u8(f):
    return read_ubytes(f, 8)

def read_constant_pool(f, clazz):
    constant_pool = [{}]
    for i in range(1, clazz['constant_pool_count']):
        tag = read_u1(f)
        print(f"{tag=}")
        if tag == CONSTANT_METHODREF or tag == CONSTANT_FIELDREF or tag == CONSTANT_INTERFACE_METHODREF:
            info = {"tag":tag}
            info["class_index"] = read_u2(f)
            info["name_and_type_index"] = read_u2(f)
            constant_pool.append(info)
            print(info)
        else:
            raise Exception(f"to be implemented {tag}")


with open("Demo.class",'rb') as f:
    clazz = {}
    clazz['magic']= hex(int.from_bytes(f.read(4),'big'))
    clazz['minor_version']= hex(int.from_bytes(f.read(2),'big'))
    clazz['major_version'] = hex(int.from_bytes(f.read(2),'big'))
    clazz['constant_pool_count'] = int.from_bytes(f.read(2),'big')
    print(f"{clazz}")
    read_constant_pool(f, clazz)


