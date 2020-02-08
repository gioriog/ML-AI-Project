import os
from os import path
import shutil

def copyFiles(src,dst,file,ext):
	with open(file) as f:
		files = f.readlines()

	# eliminate \n
	files = [f.strip() for f in files]

	# add jpg extension
	img_files = [f+ext for f in files]
        
	print(files)
	
	#sys.stdout.write("".join(files))

	# copy from src to dst
	for f in img_files:
		shutil.copy(path.join(src,f), dst)

	
'''
train_path = "comic/ImageSets/Main/train.txt"
test_path = "comic/ImageSets/Main/test.txt"

src = "comic/JPEGImages/"
dst = "comic/JPEGImages2/"

copyFiles(src,dst,train_path,".jpg")
copyFiles(src,dst,test_path,".jpg")

src = "comic/Annotations/"
dst = "comic/Annotations2/"

copyFiles(src,dst,train_path,".xml")
copyFiles(src,dst,test_path,".xml")

'''



#WATERCOLOR

train_path = "watercolor/ImageSets/Main/train.txt"
test_path = "watercolor/ImageSets/Main/test.txt"

src = "watercolor/JPEGImages/"
dst = "watercolor/JPEGImages2/"

copyFiles(src,dst,train_path,".jpg")
copyFiles(src,dst,test_path,".jpg")

src = "watercolor/Annotations/"
dst = "watercolor/Annotations2/"

copyFiles(src,dst,train_path,".xml")
copyFiles(src,dst,test_path,".xml")

