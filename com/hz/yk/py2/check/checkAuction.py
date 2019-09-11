import os
import os.path
import re

packDir='/Users/ykdsg/svn_workspace/misc/misc_0905/20130905_15627_1/misccenter/misccenter-server/src/main/java/com/taobao/misccenter/auction'
p1=re.compile(r"misccenter\.((?!auction)\w)+\b")
p2=re.compile(r"misccenter\.((?!domain)\w)+\b")
p3=re.compile(r"misccenter\.((?!utils)\w)+\b")

def processDirectory(args,dirname,filenames):
	# print 'Directory',dirname
	for filename in filenames:
		if os.path.splitext(filename)[1]=='.java':
			# print 'file',filename
			fileObj=open(dirname+ "/"+filename)
			hasOther=False
			for line in fileObj:
				if p1.search(line) and p2.search(line) and p3.search(line):
					hasOther=True
					print line

			if hasOther:
				print 'file:',filename


def search():
	os.path.walk(packDir,processDirectory,None)

if __name__ == '__main__':
	search()

