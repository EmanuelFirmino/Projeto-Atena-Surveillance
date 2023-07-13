#!/usr/bin/env python

# 217.91.58.189

# /axis-cgi/com/ptz.cgi?rpan=10 move axis http://206.40.97.180/

from athena.settings.const import athena_attributes

from requests import get, exceptions
import cv2    as     opencv
import sys

class megaPixel:
    def __init__(self):
        self.host       = athena_attributes.server
        self.port       = athena_attributes.port
        self.fx         = athena_attributes.fx
        self.fy         = athena_attributes.fy
        self.windowName = '{}:{}'.format(self.host, self.port)
        self.payload    = f'http://{self.host}:{self.port}/mjpg/video.mjpg'
        self.move       = f'http://{self.host}:{self.port}/axis-cgi/com/ptz.cgi?camera=1'


    def getFrame(self, frame):
        width   = int(800 * self.fx)
        height  = int(600 * self.fy)
        return opencv.resize(frame, (width, height), interpolation=opencv.INTER_AREA)

    def ptzMove(self, key):
        if key == 'w':
            get(self.move+'&move=up')
        if key == 's':
            get(self.move+'&move=down')
        if key == 'a':
            get(self.move+'&move=left')
        if key == 'd':
            get(self.move+'&move=right')
        if key == 'z':
            get(self.move+'&rzoom=500')
        if key == 'x':
            get(self.move+'&rzoom=-500')

    def run(self):
        capFrame = opencv.VideoCapture(self.payload)

        try:
            while True:
                frame = capFrame.read()[1]
                opencv.imshow(self.windowName, self.getFrame(frame))
                opencv.namedWindow(self.windowName, opencv.WND_PROP_FULLSCREEN)
                opencv.setWindowProperty(self.windowName, opencv.WND_PROP_FULLSCREEN, opencv.WINDOW_FULLSCREEN)
                key = chr(opencv.waitKey(1) & 0xff)
                self.ptzMove(key)

        except KeyboardInterrupt:
            capFrame.release()
            opencv.destroyAllWindows()

    
    def __str__(self):
        return f'{self.host}:{self.port}'       