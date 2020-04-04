# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('./capture.jpg',cv2.IMREAD_COLOR)
kirin = cv2.imread('./gschool.jpeg',cv2.IMREAD_COLOR)
#色の補正
image = image[:,:,[2,1,0]]
kirin = kirin[:,:,[2,1,0]]
height,width = kirin.shape[:2] #キリンの画像の縦と横の長さを取得
image[100:height + 100, 200:width + 200] = kirin #貼り付け
plt.imshow(image) #表示
plt.show()
