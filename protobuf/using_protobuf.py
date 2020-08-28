# from python.person_pb2 import *
from google.protobuf import text_format
from protos.people_pb2 import *

pers = People()

p1 = pers.person.add()
p1.id = 1
p1.name = 'yy'

p2 = pers.person.add()
p2.id = 2
p2.name = 'pyy'

data = pers.SerializeToString()

with open('person_py.bin', 'wb') as f:
  f.write(data)

with open('person_py.config', 'w') as f:
  f.write(text_format.MessageToString(pers))

with open('person_py.bin', 'rb') as f:
  data1 = f.read()

pers1 = People()
pers1.ParseFromString(data1)
for p in pers1.person:
  print(p.id, p.name)

with open('person_cpp.bin', 'rb') as f:
  data1 = f.read()

pers1 = People()
pers1.ParseFromString(data1)
for p in pers1.person:
  print(p.id, p.name)
