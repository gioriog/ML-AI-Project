import os
from os import path
import shutil

def copyFiles(src,dst,file):
	with open(file) as f:
		files = f.readlines()

	# eliminate \n
	files = [f.strip() for f in files]

	# add jpg extension
	files = [f+".jpg" for f in files]

	print(files)
	
	#sys.stdout.write("".join(files))

	# copy from src to dst
	for f in files:
		shutil.copy(path.join(src,f), dst)

train_path = "ML-AI-Project/build/darknet/x64/data/watercolor/ImageSets/Main/train.txt"
test_path = "ML-AI-Project/build/darknet/x64/data/watercolor/ImageSets/Main/test.txt"

src = "ML-AI-Project/build/darknet/x64/data/watercolor/JPEGImages"
dst = "ML-AI-Project/build/darknet/x64/data/watercolor/JPEGImages2/"

copyFiles(src,dst,train_path)
copyFiles(src,dst,test_path)

