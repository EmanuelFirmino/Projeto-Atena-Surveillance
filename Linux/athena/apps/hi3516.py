#!/usr/bin/env python

from athena.settings.stdout_color import stdout_colors
from athena.settings.const import athena_attributes

import cv2 as opencv
import requests
import shutil
import sys

class hi3516_manufacturer:
    def __init__(self):
        self.host = athena_attributes.server
        self.fx = athena_attributes.fx
        self.fy = athena_attributes.fy
        self.port = athena_attributes.port
        self.frame_key = athena_attributes.frame_chunk
        self.payload = 'http://{}:{}/webcapture.jpg?command=snap&channel=1'.format(self.host, self.port)
    
    def getFrame(self):
        req = requests.get(self.payload, stream=True)

        with open(athena_attributes.frame_chunk, 'wb') as chunk:
            shutil.copyfileobj(req.raw, chunk)

        return opencv.resize(opencv.imread(self.frame_key), None, fx=self.fx, fy=self.fy, interpolation=opencv.INTER_CUBIC)

    def run(self):

        try:
            requests.get(self.payload, stream=True, timeout=0x5)

            while True:
                try:
                    img=self.getFrame()
                    opencv.imshow('{}:{}'.format(self.host, self.port), img)
                    opencv.waitKey(athena_attributes.delay_ms)

                except KeyboardInterrupt:
                    sys.exit()
        
            opencv.destroyAllWindows()
    
        except requests.exceptions.ConnectTimeout:
            sys.exit()

        except requests.exceptions.ConnectionError:
            sys.exit()

    def __str__(self):
        return '<{}:{}>'.format(self.host, self.port)