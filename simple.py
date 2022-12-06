import pprint
import io
import ctypes


pp = pprint.PrettyPrinter(indent=4)
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

def read_bytes(f, count):
    return f.read(count)

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
        if tag == CONSTANT_METHODREF or tag == CONSTANT_FIELDREF or tag == CONSTANT_INTERFACE_METHODREF:
            info = {"tag":tag}
            info["class_index"] = read_u2(f)
            info["name_and_type_index"] = read_u2(f)
            constant_pool.append(info)
        elif tag == CONSTANT_STRING:
            info = {"tag":tag}
            info["string_index"] = read_u2(f)
            constant_pool.append(info)
        elif tag == CONSTANT_CLASS:
            info = {"tag":tag}
            info["name_index"] = read_u2(f)
            constant_pool.append(info)
        elif tag == CONSTANT_NAME_AND_TYPE:
            info = {"tag":tag}
            info["name_index"] = read_u2(f)
            info["descriptor_index"] = read_u2(f)
            constant_pool.append(info)
        elif tag == CONSTANT_UTF8:
            info = {"tag":tag}
            info["length"] = read_u2(f)
            info["value"] = read_bytes(f, info["length"]).decode("utf-8")
            constant_pool.append(info)
        else:
            raise Exception(f"to be implemented {tag}")
    return constant_pool

def at_pool(clazz,index):
    return clazz['constant_pool'][index]

def desc_bytes(bs):
    for b in bs:
        print(f'\\x{b:02x}',end='')

def name_of_class(clazz, index):
    return clazz['constant_pool'][clazz['constant_pool'][index]['name_index']]['value']

def name_of_member(clazz, index):
    return clazz['constant_pool'][clazz['constant_pool'][index]['name_index']]['value']

def type_of(obj):
    if obj['type'] == 'FakePrintStream':
        return 'java/io/PrintStream'
    else:
        assert False, f'{obj=} not supported.'

getstatic = 0xb2
ldc = 0x12
invokevirtual = 0xb6
ret = 0xb1
bipush = 0x10

def execute_code(clazz, code):
    s = io.BytesIO(code)
    # \xb2\x00\x02
    # \x12\x03
    # \xb6\x00\x04
    # \xb1'
    stack = []
    while s.tell() < len(code):
        opcode = read_u1(s)
        if opcode == getstatic:
            index = read_u2(s)
            if name_of_class(clazz, at_pool(clazz,index)['class_index']) != 'java/lang/System':
                assert False, "unsupported class of a field."
            if name_of_class(clazz, at_pool(clazz,index)['name_and_type_index']) != 'out':
                assert False, "unsupported class of a field."
            stack.append({'type': 'FakePrintStream'})

        elif opcode == bipush:
            val = ctypes.c_int8(read_u1(s)).value
            stack.append({'type':'Number', 'value': val})
        elif opcode == ldc:
            index = read_u1(s)
            if  at_pool(clazz,index)['tag'] != CONSTANT_STRING:
                assert False, f"{at_pool(clazz,index)['tag']} is not supported."
            stack.append({'type':'Constant', 'value': at_pool(clazz,at_pool(clazz,index)['string_index'])['value']})
        elif opcode == invokevirtual:
            index = read_u2(s)
            method_name = name_of_class(clazz, at_pool(clazz,index)['name_and_type_index'])
            if method_name != 'println':
                assert False, f"{method_name} is not supported."
            obj = stack[-2]
            if type_of(obj) != name_of_class(clazz, at_pool(clazz,index)['class_index']):
                assert False, f'{obj} not supported.'

            val = stack[-1]
            print(val['value'])
        elif opcode == ret:
            return
        else:
            assert False, f"{hex(opcode)} to be implemented"


def execute_method(method):
    s = io.BytesIO(method['attributes'][0]['bytes'])
    code = {}
    code['max_stacks'] = read_u2(s)
    code['max_locals'] = read_u2(s)
    code['code_length'] = read_u4(s)
    code['bytes'] = read_bytes(s,code['code_length'])
    code['exception_table_length'] = read_u2(s)
    code['exception_table'] = read_bytes(s,code['exception_table_length'])
    code['attributes_count'] = read_u2(s)
    code['attributes'] = []
    for i in range(0, code['attributes_count']):
        attribute = {}
        attribute['attribute_name_index'] = read_u2(s)
        attribute['attribute_length'] = read_u4(s)
        attribute['bytes'] = read_bytes(s,attribute['attribute_length'])
        code['attributes'].append(attribute)

    # pp.pprint(method)
    # desc_bytes(code['bytes'])
    execute_code(clazz, code['bytes'])

def parse_class(filename:str) -> dict:
    clazz = {}
    with open(filename,'rb') as f:
        clazz['magic']= hex(read_u4(f))
        clazz['minor_version']= hex(read_u2(f))
        clazz['major_version'] = hex(read_u2(f))
        clazz['constant_pool_count'] = read_u2(f)
        clazz["constant_pool"] = read_constant_pool(f, clazz)
        clazz['access_flags'] = read_u2(f)
        clazz['this_class'] = read_u2(f)
        clazz['super_class'] = read_u2(f)

        clazz['interfaces_count'] = read_u2(f)
        clazz['interfaces'] = []
        for i in range(0, clazz['interfaces_count']):
            clazz['interfaces'].append(read_u2(f))

        clazz['fields_count'] = read_u2(f)
        clazz['fields ']= []
        for i in range(0, clazz['fields_count']):
            field = {}
            field['access_flags'] = read_u2(f)
            field['name_index'] = read_u2(f);
            field['descriptor_index'] = read_u2(f);
            field['attributes_count'] = read_u2(f);
            attributes = []
            field['attributes'] = attributes
            for j in range(0, field['attributes_count']):
                attribute = {}
                attribute['attribute_name_index'] = read_u2(f)
                attribute['attribute_length'] = read_u4(f)
                attribute['bytes'] = read_bytes(f,attribute['attribute_length'])
                attributes.append(attribute)
            clazz['fields'].append(field)

        clazz['methods_count'] = read_u2(f)

        clazz['methods']= []
        for i in range(0, clazz['methods_count']):
            method = {}
            method['access_flags'] = read_u2(f)
            method['name_index'] = read_u2(f);
            method['descriptor_index'] = read_u2(f);
            method['attributes_count'] = read_u2(f);
            attributes = []
            for j in range(0, method['attributes_count']):
                attribute = {}
                attribute['attribute_name_index'] = read_u2(f)
                attribute['attribute_length'] = read_u4(f)
                attribute['bytes'] = read_bytes(f,attribute['attribute_length'])
                attributes.append(attribute)
            method['attributes'] = attributes
            clazz['methods'].append(method)

        clazz['attributes_count'] = read_u2(f);
        clazz['attributes']= []
        for j in range(0, clazz['attributes_count']):
            attribute = {}
            attribute['attribute_name_index'] = read_u2(f)
            attribute['attribute_length'] = read_u4(f)
            attribute['bytes'] = read_bytes(f,attribute['attribute_length'])
            clazz['attributes'].append(attribute)
    return clazz


print("----------------execute methods---------------------")

clazz = parse_class('./Demo.class')

def find_method_by_name(clazz, name:str):
    for method in clazz['methods']:
        if clazz['constant_pool'][method['name_index']]['value'] == name:
            return method

pp.pprint(at_pool(clazz, find_method_by_name(clazz, 'main')['attributes'][0]['attribute_name_index']))
execute_method(find_method_by_name(clazz, 'main'))
