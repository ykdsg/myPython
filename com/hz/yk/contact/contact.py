__author__ = 'wuzheng.yk'

import cPickle as p
from person import *

personlistfile = 'personlist.data'
personMap = {}
per1 = person('name1', 10, 1)
personMap[per1.name]=per1
dataString=p.dumps(personMap)
f = file(personlistfile, 'a')
f.write(dataString)
f.close()

f = file(personlistfile)
storedPerson = p.load(f)
print storedPerson['name1'].sex
print storedPerson
