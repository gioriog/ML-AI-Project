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
	for f in files:
		shutil.move(path.join(src,f)+ext, dst+ext)

	
#COMIC
train_path = "/content/ML-AI-Project/build/darknet/x64/data/comic/ImageSets/Main/train.txt"
test_path = "/content/ML-AI-Project/build/darknet/x64/data/comic/ImageSets/Main/test.txt"

src = "/content/ML-AI-Project/build/darknet/x64/data/comic/JPEGImages/"
train_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/trainB/"
test_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/testB/"

copyFiles(src,train_dst,train_path,".jpg")
copyFiles(src,test_dst,test_path,".jpg")



#VOC 2007
train_path = "/content/ML-AI-Project/build/darknet/x64/data/voc/VOCdevkit/VOC2007/ImageSets/Main/train.txt"
test_path = "/content/ML-AI-Project/build/darknet/x64/data/voc/VOCdevkit/VOC2007/ImageSets/Main/test.txt"

src = "/content/ML-AI-Project/build/darknet/x64/data/voc/VOCdevkit/VOC2007/JPEGImages/"
train_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/trainA/"
test_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/testA/"

copyFiles(src,train_dst,train_path,".jpg")
copyFiles(src,test_dst,test_path,".jpg")


#VOC 2012
train_path = "/content/ML-AI-Project/build/darknet/x64/data/voc/VOCdevkit/VOC2012/ImageSets/Main/train.txt"
#test_path = "/content/ML-AI-Project/build/darknet/x64/data/voc/VOCdevkit/VOC2012/ImageSets/Main/test.txt"

src = "/content/ML-AI-Project/build/darknet/x64/data/voc/VOCdevkit/VOC2012/JPEGImages/"
train_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/trainA/"
#test_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/TestA/"

copyFiles(src,train_dst,train_path,".jpg")
#copyFiles(src,test_dst,test_path,".jpg")





#WATERCOLOR
train_path = "/content/ML-AI-Project/build/darknet/x64/data/watercolor/ImageSets/Main/train.txt"
test_path = "/content/ML-AI-Project/build/darknet/x64/data/watercolor/ImageSets/Main/test.txt"

src = "/content/ML-AI-Project/build/darknet/x64/data/watercolor/JPEGImages/"
train_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/trainA/"
test_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/testA/"

copyFiles(src,train_dst,train_path,".jpg")
copyFiles(src,test_dst,test_path,".jpg")




#CLIPART
train_path = "/content/ML-AI-Project/build/darknet/x64/data/clipart/ImageSets/Main/train.txt"
test_path = "/content/ML-AI-Project/build/darknet/x64/data/clipart/ImageSets/Main/test.txt"

src = "/content/ML-AI-Project/build/darknet/x64/data/clipart/JPEGImages/"
train_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/trainA/"
test_dst = "/content/pytorch-CycleGAN-and-pix2pix/datasets/Proj/testA/"

copyFiles(src,train_dst,train_path,".jpg")
copyFiles(src,test_dst,test_path,".jpg")
