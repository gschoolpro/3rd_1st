# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
#画像データ読み込み
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
#長方形と円の描画
cv2.rectangle(image,(30,60),(420,360),(255,100,100),thickness=5)
cv2.circle(image,(400,400),100,(255,0,0),thickness=5)
#文字の表示
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,"this is a sample picture.",(300,700),font ,1,(0,0,255),thickness=3)
#画像の表示と保存
image = image[:,:,[2,1,0]]
plt.imshow(image)
plt.show()
plt.imsave('image_in_rectangle.png',image)
