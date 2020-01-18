import os
import shutil
import time

next=5000
last=40000
while 1:
	src="/content/darknet/backup/yolov3-voc_"+str(next)+".weights"
	dest="/content/gdrive/My\ Drive/darknet/weights/yolov3-voc_"+str(next)+".weights"
	if os.path.exists(src) :
		shutil.copy(src,dest)
                next+=5000
        else:
                time.sleep(5*60)
                
	if next==last:
		break
		
	
