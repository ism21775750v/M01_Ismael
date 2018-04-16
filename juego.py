from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True



green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def thermometer():

    W = white
    R = red
    O= nothing

    logo = [
    O, O, W, W, W, W, O, O,
    O, O, W, R, R, W, O, O,
    O, O, W, R, R, W, O, O,
    O, O, W, R, R, W, O, O,
    O, O, W, R, R, W, O, O,
    O, O, W, R, R, W, O, O,
    O, O, W, R, R, W, O, O,
    O, W, W, W, W, W, W, O,
    ]
    return logo

images = [thermometer]
count = 0



