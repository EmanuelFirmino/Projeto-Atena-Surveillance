#!/usr/bin/env python

class stdout_colors:
    def red(text):
        return '\033[0;49;91m{}\033[0m'.format(text)
    def blue(text):
        return '\033[0;49;34m{}\033[0m'.format(text)
    def green(text):
        return '\033[0;49;92m{}\033[0m'.format(text)
    def red_cover(text):
        return '\033[7;49;91m{}\033[0m'.format(text)
    def blue_cover(text):
        return '\033[7;49;34m{}\033[0m'.format(text)
    def green_cover(text):
        return '\033[7;49;92m{}\033[0m'.format(text)