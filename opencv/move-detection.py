import cv2
import time

cap = cv2.VideoCapture(0)

before = None
cycle = 20
i = 0
n = 0
print(cap.get(cv2.CAP_PROP_FPS))

while True:
    
    # OpenCVでWebカメラの画像を取り込む
    ret, frame = cap.read()
    
    # 加工なし画像を表示する
    #cv2.imshow('Raw Frame', frame)

    # 取り込んだフレームに対して差分をとって動いているところが明るい画像を作る
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if before is None:
        before = gray.copy().astype('float')
        continue
    # 現フレームと前フレームの加重平均を使うと良いらしい
    cv2.accumulateWeighted(gray, before, 0.5)
    mdframe = cv2.absdiff(gray, cv2.convertScaleAbs(before))
    # 動いているところが明るい画像を表示する
    #cv2.imshow('MotionDetected Frame', mdframe)

    # 動いているエリアの面積を計算してちょうどいい検出結果を抽出する
    thresh = cv2.threshold(mdframe, 3, 255, cv2.THRESH_BINARY)[1]
    
    # 輪郭データに変換しくれるfindContours
    image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    target = contours[0]
    for cnt in contours:
        #輪郭の面積を求めてくれるcontourArea
        area = cv2.contourArea(cnt)
        if max_area < area and area < 10000 and area > 1000:
            max_area = area;
            target = cnt

    # 動いているエリアのうちそこそこの大きさのものがあればそれを矩形で表示する
    if max_area >= 5000 and n >= cycle:
        start = time.time()
        n = 0
        x,y,w,h = cv2.boundingRect(target)
        areaframe = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        i += 1
        cv2.imwrite('/workspace/host/data/photo_' + str(i) + '.jpg',areaframe)
        print("detection_" + str(i))
        elapsed_time = time.time() - start
        print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    n += 1
    #cv2.imshow('MotionDetected Area Frame', areaframe)
    
    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    #k = cv2.waitKey(1)
    #if k == 27:
        #break

# キャプチャをリリースして、ウィンドウをすべて閉じる
#cap.release()
#cv2.destroyAllWindows()