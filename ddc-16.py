# 16
import lib_sl
import random
import time

cs = [[255,255,000,000,000,255],[000,255,255,255,000,000],[000,000,000,255,255,255]]

def rc():
  return random.randint(0,5)

def rid():
    return [random.randint(0,8),random.randint(0,6)]


while 1:
    lib_sl.speedfade(0,0,0,0,170,1000)
    lib_sl.speedfade(0,1,0,0,170,1000)
    lib_sl.speedfade(0,2,0,0,170,1000)
    lib_sl.speedfade(0,3,0,0,170,1000)
    lib_sl.speedfade(0,4,0,0,170,1000)
    lib_sl.speedfade(0,5,0,0,170,1000)
    lib_sl.speedfade(1,0,0,0,170,1000)
    lib_sl.speedfade(1,1,0,0,170,1000)
    lib_sl.speedfade(1,2,0,0,170,1000)
    lib_sl.speedfade(1,3,0,0,170,1000)
    lib_sl.speedfade(1,4,0,0,170,1000)
    lib_sl.speedfade(1,5,0,0,170,1000)
    lib_sl.speedfade(2,0,0,0,170,1000)
    lib_sl.speedfade(2,1,0,0,170,1000)
    lib_sl.speedfade(2,2,0,0,170,1000)
    lib_sl.speedfade(2,3,0,0,170,1000)
    lib_sl.speedfade(2,4,0,0,170,1000)
    lib_sl.speedfade(2,5,0,0,170,1000)
    lib_sl.speedfade(3,0,0,0,170,1000)
    lib_sl.speedfade(3,1,0,0,170,1000)
    lib_sl.speedfade(3,2,0,0,170,1000)
    lib_sl.speedfade(3,3,0,0,170,1000)
    lib_sl.speedfade(3,4,0,0,170,1000)
    lib_sl.speedfade(3,5,0,0,170,1000)
    lib_sl.speedfade(4,0,0,0,170,1000)
    lib_sl.speedfade(4,1,0,0,170,1000)
    lib_sl.speedfade(4,2,0,0,170,1000)
    lib_sl.speedfade(4,3,0,0,170,1000)
    lib_sl.speedfade(4,4,0,0,170,1000)
    lib_sl.speedfade(4,5,0,0,170,1000)
    lib_sl.speedfade(5,0,0,0,170,1000)
    lib_sl.speedfade(5,1,0,0,170,1000)
    lib_sl.speedfade(5,2,0,0,170,1000)
    lib_sl.speedfade(5,3,0,0,170,1000)
    lib_sl.speedfade(5,4,0,0,170,1000)
    lib_sl.speedfade(5,5,0,0,170,1000)
    lib_sl.speedfade(6,0,0,0,170,1000)
    lib_sl.speedfade(6,1,0,0,170,1000)
    lib_sl.speedfade(6,2,0,0,170,1000)
    lib_sl.speedfade(6,3,0,0,170,1000)
    lib_sl.speedfade(6,4,0,0,170,1000)
    lib_sl.speedfade(6,5,0,0,170,1000)
    lib_sl.speedfade(7,0,0,0,170,1000)
    lib_sl.speedfade(7,1,0,0,170,1000)
    lib_sl.speedfade(7,2,0,0,170,1000)
    lib_sl.speedfade(7,3,0,0,170,1000)
    lib_sl.speedfade(7,4,0,0,170,1000)
    lib_sl.speedfade(7,5,0,0,170,1000)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(1,5,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(7,5,0,0,0)

    time.sleep(0.8)

    lib_sl.speedfade(0,0,0,0,255,235)
    lib_sl.speedfade(0,1,0,0,255,235)
    lib_sl.speedfade(1,0,0,0,255,235)

    lib_sl.speedfade(1,1,0,0,255,235)
    lib_sl.speedfade(2,0,0,0,255,235)
    lib_sl.speedfade(2,1,0,0,255,235)

    lib_sl.speedfade(3,0,0,0,255,235)
    lib_sl.speedfade(3,1,0,0,255,235)
    lib_sl.speedfade(4,0,0,0,255,235)
    lib_sl.speedfade(4,1,0,0,255,235)

    lib_sl.speedfade(5,0,0,0,255,235)
    lib_sl.speedfade(5,1,0,0,255,235)
    lib_sl.speedfade(6,1,0,0,255,235)

    lib_sl.speedfade(6,0,0,0,255,235)
    lib_sl.speedfade(7,0,0,0,255,235)
    lib_sl.speedfade(7,1,0,0,255,235)

    lib_sl.speedfade(0,2,0,0,255,235)
    lib_sl.speedfade(0,3,0,0,255,235)
    lib_sl.speedfade(1,2,0,0,255,235)

    lib_sl.speedfade(1,3,0,0,255,235)
    lib_sl.speedfade(2,2,0,0,255,235)
    lib_sl.speedfade(2,3,0,0,255,235)

    lib_sl.speedfade(3,2,0,0,255,235)
    lib_sl.speedfade(3,3,0,0,255,235)
    lib_sl.speedfade(4,2,0,0,255,235)
    lib_sl.speedfade(4,3,0,0,255,235)

    lib_sl.speedfade(5,2,0,0,255,235)
    lib_sl.speedfade(5,3,0,0,255,235)
    lib_sl.speedfade(6,3,0,0,255,235)

    lib_sl.speedfade(6,2,0,0,255,235)
    lib_sl.speedfade(7,2,0,0,255,235)
    lib_sl.speedfade(7,3,0,0,255,235)

    lib_sl.speedfade(0,4,0,0,255,235)
    lib_sl.speedfade(0,5,0,0,255,235)
    lib_sl.speedfade(1,5,0,0,255,235)

    lib_sl.speedfade(1,4,0,0,255,235)
    lib_sl.speedfade(2,4,0,0,255,235)
    lib_sl.speedfade(2,5,0,0,255,235)

    lib_sl.speedfade(3,4,0,0,255,235)
    lib_sl.speedfade(3,5,0,0,255,235)
    lib_sl.speedfade(4,4,0,0,255,235)
    lib_sl.speedfade(4,5,0,0,255,235)

    lib_sl.speedfade(5,4,0,0,255,235)
    lib_sl.speedfade(5,5,0,0,255,235)
    lib_sl.speedfade(6,4,0,0,255,235)

    lib_sl.speedfade(7,4,0,0,255,253)
    lib_sl.speedfade(6,5,0,0,255,253)
    lib_sl.speedfade(7,5,0,0,255,253)

    time.sleep(0.023)

    lib_sl.speedfade(0,0,0,0,0,1000)
    lib_sl.speedfade(0,1,0,0,0,1000)
    lib_sl.speedfade(1,0,0,0,0,1000)

    lib_sl.speedfade(1,1,0,0,0,1000)
    lib_sl.speedfade(2,0,0,0,0,1000)
    lib_sl.speedfade(2,1,0,0,0,1000)

    lib_sl.speedfade(3,0,0,0,0,1000)
    lib_sl.speedfade(3,1,0,0,0,1000)
    lib_sl.speedfade(4,0,0,0,0,1000)
    lib_sl.speedfade(4,1,0,0,0,1000)

    lib_sl.speedfade(5,0,0,0,0,1000)
    lib_sl.speedfade(5,1,0,0,0,1000)
    lib_sl.speedfade(6,1,0,0,0,1000)

    lib_sl.speedfade(6,0,0,0,0,1000)
    lib_sl.speedfade(7,0,0,0,0,1000)
    lib_sl.speedfade(7,1,0,0,0,1000)

    lib_sl.speedfade(0,2,0,0,0,1000)
    lib_sl.speedfade(0,3,0,0,0,1000)
    lib_sl.speedfade(1,2,0,0,0,1000)

    lib_sl.speedfade(1,3,0,0,0,1000)
    lib_sl.speedfade(2,2,0,0,0,1000)
    lib_sl.speedfade(2,3,0,0,0,1000)

    lib_sl.speedfade(3,2,0,0,0,1000)
    lib_sl.speedfade(3,3,0,0,0,1000)
    lib_sl.speedfade(4,2,0,0,0,1000)
    lib_sl.speedfade(4,3,0,0,0,1000)

    lib_sl.speedfade(5,2,0,0,0,1000)
    lib_sl.speedfade(5,3,0,0,0,1000)
    lib_sl.speedfade(6,3,0,0,0,1000)

    lib_sl.speedfade(6,2,0,0,0,1000)
    lib_sl.speedfade(7,2,0,0,0,1000)
    lib_sl.speedfade(7,3,0,0,0,1000)

    lib_sl.speedfade(0,4,0,0,0,1000)
    lib_sl.speedfade(0,5,0,0,0,1000)
    lib_sl.speedfade(1,5,0,0,0,1000)

    lib_sl.speedfade(1,4,0,0,0,1000)
    lib_sl.speedfade(2,4,0,0,0,1000)
    lib_sl.speedfade(2,5,0,0,0,1000)

    lib_sl.speedfade(3,4,0,0,0,1000)
    lib_sl.speedfade(3,5,0,0,0,1000)
    lib_sl.speedfade(4,4,0,0,0,1000)
    lib_sl.speedfade(4,5,0,0,0,1000)

    lib_sl.speedfade(5,4,0,0,0,1000)
    lib_sl.speedfade(5,5,0,0,0,1000)
    lib_sl.speedfade(6,4,0,0,0,1000)

    lib_sl.speedfade(7,4,0,0,0,1000)
    lib_sl.speedfade(6,5,0,0,0,1000)
    lib_sl.speedfade(7,5,0,0,0,1000)

    time.sleep(0.235)

    lib_sl.speedfade(0,0,0,0,255,800)
    lib_sl.speedfade(0,1,0,0,255,800)
    lib_sl.speedfade(1,0,0,0,255,800)
    lib_sl.speedfade(0,2,0,0,255,800)
    lib_sl.speedfade(0,3,0,0,255,800)
    lib_sl.speedfade(1,2,0,0,255,800)
    lib_sl.speedfade(0,4,0,0,255,800)
    lib_sl.speedfade(0,5,0,0,255,800)
    lib_sl.speedfade(1,5,0,0,255,800)

    lib_sl.send(0,0,0,0,255)
    lib_sl.send(0,1,0,0,255)
    lib_sl.send(1,0,0,0,255)
    lib_sl.send(0,2,0,0,255)
    lib_sl.send(0,3,0,0,255)
    lib_sl.send(1,2,0,0,255)
    lib_sl.send(0,4,0,0,255)
    lib_sl.send(0,5,0,0,255)
    lib_sl.send(1,5,0,0,255)

    lib_sl.speedfade(1,1,0,0,255,800)
    lib_sl.speedfade(2,0,0,0,255,800)
    lib_sl.speedfade(2,1,0,0,255,800)
    lib_sl.speedfade(1,3,0,0,255,800)
    lib_sl.speedfade(2,2,0,0,255,800)
    lib_sl.speedfade(2,3,0,0,255,800)
    lib_sl.speedfade(1,4,0,0,255,800)
    lib_sl.speedfade(2,4,0,0,255,800)
    lib_sl.speedfade(2,5,0,0,255,800)

    lib_sl.send(1,1,0,0,255)
    lib_sl.send(2,0,0,0,255)
    lib_sl.send(2,1,0,0,255)
    lib_sl.send(1,3,0,0,255)
    lib_sl.send(2,2,0,0,255)
    lib_sl.send(2,3,0,0,255)
    lib_sl.send(1,4,0,0,255)
    lib_sl.send(2,4,0,0,255)
    lib_sl.send(2,5,0,0,255)

    lib_sl.speedfade(3,0,0,0,255,800)
    lib_sl.speedfade(3,1,0,0,255,800)
    lib_sl.speedfade(4,0,0,0,255,800)
    lib_sl.speedfade(4,1,0,0,255,800)
    lib_sl.speedfade(3,2,0,0,255,800)
    lib_sl.speedfade(3,3,0,0,255,800)
    lib_sl.speedfade(4,2,0,0,255,800)
    lib_sl.speedfade(4,3,0,0,255,800)
    lib_sl.speedfade(3,4,0,0,255,800)
    lib_sl.speedfade(3,5,0,0,255,800)
    lib_sl.speedfade(4,4,0,0,255,800)
    lib_sl.speedfade(4,5,0,0,255,800)

    lib_sl.send(3,0,0,0,255)
    lib_sl.send(3,1,0,0,255)
    lib_sl.send(4,0,0,0,255)
    lib_sl.send(4,1,0,0,255)
    lib_sl.send(3,2,0,0,255)
    lib_sl.send(3,3,0,0,255)
    lib_sl.send(4,2,0,0,255)
    lib_sl.send(4,3,0,0,255)
    lib_sl.send(3,4,0,0,255)
    lib_sl.send(3,5,0,0,255)
    lib_sl.send(4,4,0,0,255)
    lib_sl.send(4,5,0,0,255)

    lib_sl.speedfade(5,0,0,0,255,800)
    lib_sl.speedfade(5,1,0,0,255,800)
    lib_sl.speedfade(6,1,0,0,255,800)
    lib_sl.speedfade(5,2,0,0,255,800)
    lib_sl.speedfade(5,3,0,0,255,800)
    lib_sl.speedfade(6,3,0,0,255,800)
    lib_sl.speedfade(5,4,0,0,255,800)
    lib_sl.speedfade(5,5,0,0,255,800)
    lib_sl.speedfade(6,4,0,0,255,800)

    lib_sl.send(5,0,0,0,255)
    lib_sl.send(5,1,0,0,255)
    lib_sl.send(6,1,0,0,255)
    lib_sl.send(5,2,0,0,255)
    lib_sl.send(5,3,0,0,255)
    lib_sl.send(6,3,0,0,255)
    lib_sl.send(5,4,0,0,255)
    lib_sl.send(5,5,0,0,255)
    lib_sl.send(6,4,0,0,255)

    lib_sl.speedfade(6,0,0,0,255,800)
    lib_sl.speedfade(7,0,0,0,255,800)
    lib_sl.speedfade(7,1,0,0,255,800)
    lib_sl.speedfade(6,2,0,0,255,800)
    lib_sl.speedfade(7,2,0,0,255,800)
    lib_sl.speedfade(7,3,0,0,255,800)
    lib_sl.speedfade(7,4,0,0,255,800)
    lib_sl.speedfade(6,5,0,0,255,800)
    lib_sl.speedfade(7,5,0,0,255,800)

    lib_sl.send(6,0,0,0,255)
    lib_sl.send(7,0,0,0,255)
    lib_sl.send(7,1,0,0,255)
    lib_sl.send(6,2,0,0,255)
    lib_sl.send(7,2,0,0,255)
    lib_sl.send(7,3,0,0,255)
    lib_sl.send(7,4,0,0,255)
    lib_sl.send(6,5,0,0,255)
    lib_sl.send(7,5,0,0,255)

    lib_sl.speedfade(0,0,0,255,0,800)
    lib_sl.speedfade(0,1,0,255,0,800)
    lib_sl.speedfade(1,0,0,255,0,800)
    lib_sl.speedfade(0,2,0,255,0,800)
    lib_sl.speedfade(0,3,0,255,0,800)
    lib_sl.speedfade(1,2,0,255,0,800)
    lib_sl.speedfade(0,4,0,255,0,800)
    lib_sl.speedfade(0,5,0,255,0,800)
    lib_sl.speedfade(1,5,0,255,0,800)

    lib_sl.send(0,0,0,255,0)
    lib_sl.send(0,1,0,255,0)
    lib_sl.send(1,0,0,255,0)
    lib_sl.send(0,2,0,255,0)
    lib_sl.send(0,3,0,255,0)
    lib_sl.send(1,2,0,255,0)
    lib_sl.send(0,4,0,255,0)
    lib_sl.send(0,5,0,255,0)
    lib_sl.send(1,5,0,255,0)

    lib_sl.speedfade(1,1,0,255,0,800)
    lib_sl.speedfade(2,0,0,255,0,800)
    lib_sl.speedfade(2,1,0,255,0,800)
    lib_sl.speedfade(1,3,0,255,0,800)
    lib_sl.speedfade(2,2,0,255,0,800)
    lib_sl.speedfade(2,3,0,255,0,800)
    lib_sl.speedfade(1,4,0,255,0,800)
    lib_sl.speedfade(2,4,0,255,0,800)
    lib_sl.speedfade(2,5,0,255,0,800)

    lib_sl.send(1,1,0,255,0)
    lib_sl.send(2,0,0,255,0)
    lib_sl.send(2,1,0,255,0)
    lib_sl.send(1,3,0,255,0)
    lib_sl.send(2,2,0,255,0)
    lib_sl.send(2,3,0,255,0)
    lib_sl.send(1,4,0,255,0)
    lib_sl.send(2,4,0,255,0)
    lib_sl.send(2,5,0,255,0)

    lib_sl.speedfade(3,0,0,255,0,800)
    lib_sl.speedfade(3,1,0,255,0,800)
    lib_sl.speedfade(4,0,0,255,0,800)
    lib_sl.speedfade(4,1,0,255,0,800)
    lib_sl.speedfade(3,2,0,255,0,800)
    lib_sl.speedfade(3,3,0,255,0,800)
    lib_sl.speedfade(4,2,0,255,0,800)
    lib_sl.speedfade(4,3,0,255,0,800)
    lib_sl.speedfade(3,4,0,255,0,800)
    lib_sl.speedfade(3,5,0,255,0,800)
    lib_sl.speedfade(4,4,0,255,0,800)
    lib_sl.speedfade(4,5,0,255,0,800)

    lib_sl.send(3,0,0,255,0)
    lib_sl.send(3,1,0,255,0)
    lib_sl.send(4,0,0,255,0)
    lib_sl.send(4,1,0,255,0)
    lib_sl.send(3,2,0,255,0)
    lib_sl.send(3,3,0,255,0)
    lib_sl.send(4,2,0,255,0)
    lib_sl.send(4,3,0,255,0)
    lib_sl.send(3,4,0,255,0)
    lib_sl.send(3,5,0,255,0)
    lib_sl.send(4,4,0,255,0)
    lib_sl.send(4,5,0,255,0)

    lib_sl.speedfade(5,0,0,255,0,800)
    lib_sl.speedfade(5,1,0,255,0,800)
    lib_sl.speedfade(6,1,0,255,0,800)
    lib_sl.speedfade(5,2,0,255,0,800)
    lib_sl.speedfade(5,3,0,255,0,800)
    lib_sl.speedfade(6,3,0,255,0,800)
    lib_sl.speedfade(5,4,0,255,0,800)
    lib_sl.speedfade(5,5,0,255,0,800)
    lib_sl.speedfade(6,4,0,255,0,800)

    lib_sl.send(5,0,0,255,0)
    lib_sl.send(5,1,0,255,0)
    lib_sl.send(6,1,0,255,0)
    lib_sl.send(5,2,0,255,0)
    lib_sl.send(5,3,0,255,0)
    lib_sl.send(6,3,0,255,0)
    lib_sl.send(5,4,0,255,0)
    lib_sl.send(5,5,0,255,0)
    lib_sl.send(6,4,0,255,0)

    lib_sl.speedfade(6,0,0,255,0,800)
    lib_sl.speedfade(7,0,0,255,0,800)
    lib_sl.speedfade(7,1,0,255,0,800)
    lib_sl.speedfade(6,2,0,255,0,800)
    lib_sl.speedfade(7,2,0,255,0,800)
    lib_sl.speedfade(7,3,0,255,0,800)
    lib_sl.speedfade(7,4,0,255,0,800)
    lib_sl.speedfade(6,5,0,255,0,800)
    lib_sl.speedfade(7,5,0,255,0,800)

    lib_sl.send(6,0,0,255,0)
    lib_sl.send(7,0,0,255,0)
    lib_sl.send(7,1,0,255,0)
    lib_sl.send(6,2,0,255,0)
    lib_sl.send(7,2,0,255,0)
    lib_sl.send(7,3,0,255,0)
    lib_sl.send(7,4,0,255,0)
    lib_sl.send(6,5,0,255,0)
    lib_sl.send(7,5,0,255,0)

    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,0,0,0,0)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(1,2,0,0,0)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(1,5,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(6,1,0,0,0)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(6,3,0,0,0)
    lib_sl.send(6,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(7,5,0,0,0)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
    time.sleep(0.5)
