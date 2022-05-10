#import boto3
#import json
import cv2
#import datetime
import time
#import numpy as np
import os
#import argparse
import shutil
#import time
#from PIL import Image
import human_real


#def photo_up():         #AWS S3
    #s3 = boto3.resource('s3',region_name=REGION,aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    #data = open('/workspace/host/' + IMG_NAME, 'rb')
    #s3.Bucket(BUCKET_NAME).put_object(Key=IMG_NAME, Body=data)

while True:
    #if (os.path.isfile('/workspace/host/opencv/photo.jpg')):
    if (os.path.isfile('/workspace/host/darknet-nnpack/trigger.txt')):    
        c = cv2.VideoCapture(0)
        r, img = c.read()
        cv2.imwrite('/workspace/host/0data/photo.jpg', img)
        os.system("./darknet detector test cfg/obj.data cfg/yolov3-tiny_obj2.cfg yolov3-tiny_obj2_last.weights  /workspace/host/0data/photo.jpg")
        new_path = shutil.move('/workspace/host/darknet-nnpack/predictions.jpg', '/workspace/host/photo.jpg')
        #print("Uploading")
        #photo_up()
        #print("DONE")
        os.remove('/workspace/host/0data/photo.jpg')
        os.remove('/workspace/host/darknet-nnpack/trigger.txt')