import os 
import re
import xml.etree.ElementTree as ET

os.chdir(os.path.dirname(os.path.abspath('pseudo_label.py')))

index_classes={"bicycle":0,"bird":1,"car":2,"cat":3,"dog":4,"person":5}

IN_FILE = '/content/darknet/result.txt'

# change directory 
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print("...scripting...\n")
print("root: " + parent_path)
DR_PATH = os.path.join(parent_path,'ML-AI-Project/build/darknet/x64/data/comic/labels')
ANN_PATH = os.path.join(parent_path,'ML-AI-Project/build/darknet/x64/data/comic/Annotations_Inoue')

print('Saves results in: '+ DR_PATH)
os.chdir(DR_PATH)

SEPARATOR_KEY = 'Enter Image Path:'
IMG_FORMAT = '.jpg'



def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


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

      #ANNOTATION FILE OF INOUE
      annotationfile = open (os.path.join(ANN_PATH, image_name + '.xml'), 'r')
      tree=ET.parse(annotationfile)
      root = tree.getroot()
      size = root.find('size')
      wA = int(size.find('width').text)
      hA = int(size.find('height').text)
      annotationfile.close()


      #ANNOTATION FILE MADE BY US
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
        print("Img="+image_name+ " Ann :" + str(annotations)+ "Class:"+class_name)
          
        if class_name in index_classes:
          for a in annotations:
            a=a.strip()
            if a == class_name:
              b = (float(left), float(right), float(top), float(bottom))
              bb=convert((wA,hA), b)
              
              outfile.write(str(index_classes[class_name])+ " " + " ".join([str(a) for a in bb])+ " "+ confidence+"\n")
              print(str(index_classes[class_name])+ " " + " ".join([str(a) for a in bb])+ " "+ confidence)
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





#TAKE TOP-1 DETECTION
    
train_file=open(os.path.join(parent_path,'ML-AI-Project/build/darknet/x64/data/comic/train.txt'),'r')
train_lines=train_file.readlines()
for line in train_lines:
  print("")
  print("")
  print("")
  print("")
  print("NEW FILE")
  line=line.strip()
  line=line.replace(".jpg","").split("/")
  line=line[-1]
  annotationfile = open (os.path.join(DR_PATH, line + '_1.txt'), 'r')
  real_annotations = annotationfile.readlines()
  annotationfile.close()

  annotationfile = open (os.path.join(DR_PATH, line + '.txt'), 'r')
  our_annotations = annotationfile.readlines()
  annotationfile.close()

  outfile = open (os.path.join(DR_PATH, line + '.txt'), 'w')
  for ann in real_annotations:
    ann=ann.strip()
    selected=""
    for our_ann in our_annotations:
      if our_ann.startswith(str(index_classes[ann])):
        print("Annotation: "+our_ann)
        print("Confidence: "+our_ann.split()[-1])
        if selected=="":
          selected=our_ann
          print("SELECTED:"+selected)
        else:
          our_splits=our_ann.split()
          sel_splits=selected.split()
          our_a=int(our_splits[-1])
          sel_a=int(sel_splits[-1])
          print("cikoewujcvboiwqeoljvhbewqolivuubwqeoivuuwbeqlivjwebvoiuewqbvoiwqehb "+str(our_a)+" "+str(sel_a))
          
          if our_a>sel_a:
            selected=our_ann
            print("CHANGED:"+selected)
    
    if selected!="":
      selected_splits=selected.split()
      selected_splits=selected_splits[:-1]
      outfile.write(" ".join([a for a in selected_splits]))
      print("WRITTEN ON FILE:"+ " ".join([a for a in selected_splits]))
      our_annotations.remove(selected)
              
  outfile.close()   
  
  
      
