#!/usr/bin/env python

from athena.settings.const        import athena_attributes
from athena.settings.stdout_color import stdout_colors

import argparse
import sys
import os

assert('linux' in sys.platform), "Linux module only"

if __name__ == '__main__':

    # --------------------------- Optional Arguments --------------------------

    parser = argparse.ArgumentParser(prog='athena', description='Bypass web surveillance live camera tool', epilog='by: EmanuelFirmino\n')
    parser.add_argument('-p', '--port', dest='port', help='port hosting WEB Surveillance aplication', default=80)
    parser.add_argument('-s', '--server', dest='server', help='server hosting WEB Surveillance aplication')
    parser.add_argument('-v', dest='verbose', action='count', default=0, help='verbosity level')
    parser.add_argument('-q', '--quiet', dest='quiet', action='store_true', default=False, help='supress stdout information (default: false)')
    parser.add_argument('-sB', dest='supress_banner', action='store_true', default=False, help='supress banner (default: false)')
    parser.add_argument('-fX', dest='fx', default=1, help='width increment of video capture (default: 1)')
    parser.add_argument('-fY', dest='fy', default=1, help='height increment of video capture (default: 1)')
    

    arguments = dict(parser.parse_args()._get_kwargs())

    athena_attributes.server = arguments['server']
    athena_attributes.port   = arguments['port']

    from athena.apps.megapixel import megaPixel

    athena_attributes.fx = float(arguments['fx'])
    athena_attributes.fy = float(arguments['fy'])

    megaPixel().run()
