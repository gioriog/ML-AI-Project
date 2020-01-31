import os 
import re

os.chdir(os.path.dirname(os.path.abspath('pseudo_label.py')))

IN_FILE = '/content/darknet/result.txt'

# change directory 
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print("...scripting...\n")
print("root: " + parent_path)
DR_PATH = os.path.join(parent_path,'detection-results')
print('Saves results in: '+ DR_PATH)
os.chdir(DR_PATH)

SEPARATOR_KEY = 'Enter Image Path:'
IMG_FORMAT = '.jpg'

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

        outfile.write("{} {} {} {} {} {}\n".format(class_name, float(confidence)/100, left, top, right, bottom))
      #print("{} {} {} {} {} {}\n".format(class_name, float(confidence)/100, left, top, right, bottom))


