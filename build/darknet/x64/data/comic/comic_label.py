import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

sets=['train', 'test']
# bisogna vedere se le classi elencate qui sono giuste
classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

wd = getcwd()

for image_set in sets:
    if not os.path.exists('labels/'):
        os.makedirs('labels/')
    #image_ids = open('ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    #list_file = open('%s_%s.txt'%(year, image_set), 'w')
    image_ids = open('ImageSets/Main/%s.txt'%(image_set)).readlines()
  
    list_file = open('%s.txt'%(image_set), 'w')
    for image_id in image_ids:
        image_id = image_id.strip()

        list_file.write(wd +'/JPEGImages/%s.jpg\n'%(image_id))
    list_file.close()
