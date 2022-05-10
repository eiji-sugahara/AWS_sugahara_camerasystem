for i in `seq 1  292`
do
./darknet detector test cfg/obj.data cfg/yolov3-tiny_obj2.cfg yolov3-tiny_obj2_last.weights data/face/face_$i.jpg 
done