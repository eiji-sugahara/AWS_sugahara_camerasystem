import boto3
#import json
#import cv2
#import datetime
import time
#import numpy as np
import os
#import argparse
import shutil
#import time
#from PIL import Image

REGION = 'us-east-1'
ACCESS_KEY =  'AKIA5S7ONVO7RTGPF2IG'
SECRET_KEY = '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'
IMG_NAME = 'photo.jpg'
#IMG_PASS = '~/workspace/' + IMG_NAME
BUCKET_NAME = 'egaz'
i = 0
def photo_up():         #AWS S3
    s3 = boto3.resource('s3',region_name=REGION,aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)
    data = open('/workspace/host/' + IMG_NAME, 'rb')
    s3.Bucket(BUCKET_NAME).put_object(Key=IMG_NAME, Body=data)

while True:
    for file in os.listdir('/workspace/host/data'):
        base, ext = os.path.splitext(file)
        if ext == '.jpg':
        #if (os.path.isfile('/workspace/host/opencv/photo.jpg')):
            #start = time.time()
            i += 1
            os.system("./darknet detector test cfg/obj.data cfg/yolov3-tiny_obj2.cfg yolov3-tiny_obj2_last.weights  /workspace/host/data/photo_" + str(i) + ".jpg")
            if (os.path.isfile('/workspace/host/photo.jpg')):    
                #new_path = shutil.move('/workspace/host/darknet-nnpack/predictions.jpg', '/workspace/host/photo.jpg')
                print("Uploading")
                photo_up()
                print("DONE")
                os.remove('/workspace/host/photo.jpg')
                #if (os.path.isfile('/workspace/host/data/photo_' + str(i) + '.jpg')):
            os.remove('/workspace/host/data/photo_' + str(i) + '.jpg')
            #os.remove('/workspace/host/photo.jpg')
            
            #elapsed_time = time.time() - start
            #print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
#             else