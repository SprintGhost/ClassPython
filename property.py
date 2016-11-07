#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
#"""

class Screen():
    @property
    def width(self):
        return self._witdth  #注意有下划线的，特别注意

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height



s = Screen()
s.height = 768
s.width = 1024
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
