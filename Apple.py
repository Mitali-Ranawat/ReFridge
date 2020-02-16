import cv2
import numpy as np
import mysql.connector

public class

connection = mysql.connector.connect(host='localhost',
                                         database='ipproject',
                                         user='root')



lowerBound=np.array([170,100,80])
upperBound=np.array([180,256,256])

#cam= cv2.VideoCapture(0)
kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))

font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    img=cv2.imread('2.jpg')
    #img=cv2.resize(img,(340,220))

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #cv2.imshow('HSV',imgHSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    _,conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    
    cv2.drawContours(img,conts,-1,(0,0,0),1)
    for i in range(len(conts)):
        x,y,w,h=cv2.boundingRect(conts[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
        cv2.putText(img, str(i+1),(x,y+h),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0))
        
    varr=i+1    
    print(i+1)
    

    mySql_insert_query = """UPDATE refridge_fridge SET FridgeQuantity='%s' WHERE FridgeNumber=10 and ProductID_id=3"""%(varr)
    cursor = connection.cursor()
    result = cursor.execute(mySql_insert_query,1)
    connection.commit()
    cursor.close()

    



    # cv2.imshow("maskClose",maskClose)
    # cv2.imshow("maskOpen",maskOpen)
    # cv2.imshow("mask",mask)
    cv2.imshow("cam",img)
    cv2.imwrite('image.png',img)
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()
