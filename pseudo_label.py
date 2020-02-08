import os 
import re

os.chdir(os.path.dirname(os.path.abspath('pseudo_label.py')))

index_classes={"bicycle":0,"bird":1,"car":2,"cat":3,"dog":4,"person":5}
IN_FILE = '/content/darknet/result.txt'

# change directory 
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print("...scripting...\n")
print("root: " + parent_path)
DR_PATH = os.path.join(parent_path,'ML-AI-Project/build/darknet/x64/data/comic/labels')
print('Saves results in: '+ DR_PATH)
os.chdir(DR_PATH)

SEPARATOR_KEY = 'Enter Image Path:'
IMG_FORMAT = '.jpg'

train_file=open(os.path.join(parent_path,'ML-AI-Project/build/darknet/x64/data/comic/train.txt'),'r')
train_lines=train_file.readlines()
train_file.close()

corrupted=[]


outfile = None
with open(IN_FILE) as infile:
  for line in infile:
  #for i in range(0,10):
    if SEPARATOR_KEY in line:
      if IMG_FORMAT not in line:
        break
      # get path
      image_path = re.search(SEPARATOR_KEY + '(.*)' + IMG_FORMAT,line)
      # get image name
      image_name = os.path.basename(image_path.group(1))
      # close file
      if outfile is not None:
        outfile.close()
      
      annotationfile = open (os.path.join(DR_PATH, image_name + '_1.txt'), 'r')
      annotations = annotationfile.readlines()
      annotationfile.close()
      outfile = open(os.path.join(DR_PATH, image_name + '.txt'), 'w')
    elif outfile is not None:
      class_name, info = line.split(':', 1)
      confidence, bbox = info.split('%', 1)
      # get coordianates
      bbox = bbox.replace(')','')
      #print('bbox: '+ bbox)
      if (len(bbox) != 1):
        #print('bbox: ' + bbox)
        left, top, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
        right = left + width
        bottom = top + height
        print("Img="+image_name+ "Ann :" + str(annotations)+ "Class:"+class_name)
          
        if class_name in index_classes:
          for a in annotations:
            a=a.strip()
            if a == class_name:
              outfile.write("{} {} {} {} {}\n".format(index_classes[class_name], left, top, width, height))
              print("{} {} {} {} {}\n".format(index_classes[class_name], left, top, width, height))
              break    
          #outfile.write("{} {} {} {} {}\n".format(index_classes[class_name], left, top, width, height))
        else:
          print(image_name)
      else:
        corrupted.append(image_name)
        print("NON ENTRO")
      #print("{} {} {} {} {} {}\n".format(class_name, float(confidence)/100, left, top, right, bottom))


## Eliminate corrupted files

corrupted = [ ]

train_file=open(os.path.join(parent_path,'ML-AI-Project/build/darknet/x64/data/comic/train.txt'),'w')
for line in train_lines:
  trovato=False
  for corr in corrupted:
    if line.endswith(corr+".jpg"):
      trovato=True
      print("Find image with no bbox :"+corr)
      break
  if trovato==False:
    train_file.write(line)
