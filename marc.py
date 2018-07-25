from pycpp import *

# define some model classes here:

class Command:
    def __init__(self, name, params):
        self.name, self.params = name, params

class Param:
    def __init__(self, name, dtype):
        self.name, self.dtype = name, dtype

# create some model instances (later you'll parse this from a XML/JSON):

params = {'commands': [
    Command('foo', [
        Param('i', 'int'),
        Param('s', 'string')
    ]),
    Command('bar', [])
]}

# generate code:

if __name__ == '__main__':
    with open('marc.pycpp.cpp') as f:
        gen = PyCPP(f.read(), params)
        #print(gen.get_python_code())
        print(gen.get_output())
