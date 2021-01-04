import cv2
import  winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret,frame1 = cam.read()
    ret,frame2 = cam.read()
    diff = cv2.absdiff(frame1,frame2)
    gray= cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY) # 20,255 is max size of threshold
    dilated = cv2.dilate(thresh,None,iterations=3) #dilate 3 times iteration ; diateion is oposite of threshold
    contours,_= cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #finding countors of moving area
   # cv2.drawContours(frame1,contours,-1,(0,255,0),2) #green color me countour dikhenge yani ki borders
    #for dectecting bigger counters
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        # winsound.Beep(500,200)
        winsound.PlaySound('beep.wav',winsound.SND_ASYNC)
    if cv2.waitKey(10)==ord('q'):
        break
    cv2.imshow("Camera Security",frame1)
