import os
import shutil
import time

#for
start = time.time()
	#os.system("python3 yoloface.py --image /home/pi/Desktop/face/face_" + str(i) + ".jpg --output-dir outputs/")
os.system("python3 yoloface.py --image /home/pi/Desktop/face/face_1.jpg --output-dir outputs/")
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
a=open('time.txt','a')
a.write("elapsed_time:{0}".format(elapsed_time))
a.close()