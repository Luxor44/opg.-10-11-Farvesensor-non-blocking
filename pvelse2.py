from tcs34725 import *
from machine import Pin, SoftI2C

class tcsClass:
    def _init_(self):
        self.colors_rgb = (0, )
        self.colors_rgb_list = []
    def setColors(self, rgb):
        self.colors_rgb = rgb
    def setColorsList(self, rgbList = list):
        self.colors_rgb_list = rgbList
    def returnColors(self):
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
        if i2c.scan() !=[]:
            sensor = TCS34725(i2c)
            sensor.gain(60)
            data = sensor.read(True)
            return html_rgb(data)
    def returnColorsIntList(self):
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)
        if i2c.scan() !=[]:
            sensor = TCS34725(i2c)
            sensor.gain(60)
            data = sensor.read(True)
            colors = list(html_rgb(data))
            colors = list(map(int, colors))
            
            for i in range(len(colors)):
                
                if colors[1] >= 255:
                    colors[1] = 22
            return colors
tcs = tcsClass()
tcs.setColors(tcs.returnColors())
tcs.setColorsList(tcs.returnColorsIntList())
print(tcs.colors_rgb)
print(tcs.returnColorsIntList())


