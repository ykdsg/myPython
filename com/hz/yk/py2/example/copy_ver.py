import os
import time

source ='F:/my_workspace/py_ws/*.*'
target_dir = 'F:/my_workspace/py_ws_tmp'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

target = today +"/"+now
if not os.path.exists(target):
    os.mkdir(target)
    print 'Successfully created directory',target
copy_command="cp %s %s" % (source,target)

if os.system(copy_command) == 0:
    print 'Successful backup to',target
else:
    print 'copy failed'