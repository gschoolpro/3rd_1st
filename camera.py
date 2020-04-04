# -*- coding: utf-8 -*-
import picamera     # 写真を撮るためのツール
import time

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture('capture.jpg')
