# 34
import lib_sl
import random
import time

cs = [[255,255,000,000,000,255],[000,255,255,255,000,000],[000,000,000,255,255,255]]

def rc():
  return random.randint(0,5)

def rid():
    return [random.randint(0,8),random.randint(0,6)]


while 1:
    lib_sl.send(0,0,0,0,35)
    lib_sl.send(0,1,0,0,35)
    lib_sl.send(0,2,0,0,35)
    lib_sl.send(0,3,0,0,35)
    lib_sl.send(0,4,0,0,35)
    lib_sl.send(0,5,0,0,35)
    lib_sl.send(1,0,0,0,35)
    lib_sl.send(1,1,0,0,35)
    lib_sl.send(1,2,0,0,35)
    lib_sl.send(1,3,0,0,35)
    lib_sl.send(1,4,0,0,35)
    lib_sl.send(1,5,0,0,35)
    lib_sl.send(2,0,0,0,35)
    lib_sl.send(2,1,0,0,35)
    lib_sl.send(2,2,0,0,35)
    lib_sl.send(2,3,0,0,35)
    lib_sl.send(2,4,0,0,35)
    lib_sl.send(2,5,0,0,35)
    lib_sl.send(3,0,0,0,35)
    lib_sl.send(3,1,0,0,35)
    lib_sl.send(3,2,0,0,35)
    lib_sl.send(3,3,0,0,35)
    lib_sl.send(3,4,0,0,35)
    lib_sl.send(3,5,0,0,35)
    lib_sl.send(4,0,0,0,35)
    lib_sl.send(4,1,0,0,35)
    lib_sl.send(4,2,0,0,35)
    lib_sl.send(4,3,0,0,35)
    lib_sl.send(4,4,0,0,35)
    lib_sl.send(4,5,0,0,35)
    lib_sl.send(5,0,0,0,35)
    lib_sl.send(5,1,0,0,35)
    lib_sl.send(5,2,0,0,35)
    lib_sl.send(5,3,0,0,35)
    lib_sl.send(5,4,0,0,35)
    lib_sl.send(5,5,0,0,35)
    lib_sl.send(6,0,0,0,35)
    lib_sl.send(6,1,0,0,35)
    lib_sl.send(6,2,0,0,35)
    lib_sl.send(6,3,0,0,35)
    lib_sl.send(6,4,0,0,35)
    lib_sl.send(6,5,0,0,35)
    lib_sl.send(7,0,0,0,35)
    lib_sl.send(7,1,0,0,35)
    lib_sl.send(7,2,0,0,35)
    lib_sl.send(7,3,0,0,35)
    lib_sl.send(7,4,0,0,35)
    lib_sl.send(7,5,0,0,35)
    time.sleep(1.0)
    lib_sl.speedfade(0,0,0,0,170,49)
    lib_sl.speedfade(0,1,0,0,170,49)
    lib_sl.speedfade(0,2,0,0,170,49)
    lib_sl.speedfade(0,3,0,0,170,49)
    lib_sl.speedfade(0,4,0,0,170,49)
    lib_sl.speedfade(0,5,0,0,170,49)
    lib_sl.speedfade(1,0,0,0,170,49)
    lib_sl.speedfade(1,1,0,0,170,49)
    lib_sl.speedfade(1,2,0,0,170,49)
    lib_sl.speedfade(1,3,0,0,170,49)
    lib_sl.speedfade(1,4,0,0,170,49)
    lib_sl.speedfade(1,5,0,0,170,49)
    lib_sl.speedfade(2,0,0,0,170,49)
    lib_sl.speedfade(2,1,0,0,170,49)
    lib_sl.speedfade(2,2,0,0,170,49)
    lib_sl.speedfade(2,3,0,0,170,49)
    lib_sl.speedfade(2,4,0,0,170,49)
    lib_sl.speedfade(2,5,0,0,170,49)
    lib_sl.speedfade(3,0,0,0,170,49)
    lib_sl.speedfade(3,1,0,0,170,49)
    lib_sl.speedfade(3,2,0,0,170,49)
    lib_sl.speedfade(3,3,0,0,170,49)
    lib_sl.speedfade(3,4,0,0,170,49)
    lib_sl.speedfade(3,5,0,0,170,49)
    lib_sl.speedfade(4,0,0,0,170,49)
    lib_sl.speedfade(4,1,0,0,170,49)
    lib_sl.speedfade(4,2,0,0,170,49)
    lib_sl.speedfade(4,3,0,0,170,49)
    lib_sl.speedfade(4,4,0,0,170,49)
    lib_sl.speedfade(4,5,0,0,170,49)
    lib_sl.speedfade(5,0,0,0,170,49)
    lib_sl.speedfade(5,1,0,0,170,49)
    lib_sl.speedfade(5,2,0,0,170,49)
    lib_sl.speedfade(5,3,0,0,170,49)
    lib_sl.speedfade(5,4,0,0,170,49)
    lib_sl.speedfade(5,5,0,0,170,49)
    lib_sl.speedfade(6,0,0,0,170,49)
    lib_sl.speedfade(6,1,0,0,170,49)
    lib_sl.speedfade(6,2,0,0,170,49)
    lib_sl.speedfade(6,3,0,0,170,49)
    lib_sl.speedfade(6,4,0,0,170,49)
    lib_sl.speedfade(6,5,0,0,170,49)
    lib_sl.speedfade(7,0,0,0,170,49)
    lib_sl.speedfade(7,1,0,0,170,49)
    lib_sl.speedfade(7,2,0,0,170,49)
    lib_sl.speedfade(7,3,0,0,170,49)
    lib_sl.speedfade(7,4,0,0,170,49)
    lib_sl.speedfade(7,5,0,0,170,49)
    time.sleep(4.8)
    lib_sl.speedfade(3,2,255,255,255,440)
    lib_sl.speedfade(3,3,255,255,255,440)
    lib_sl.speedfade(4,2,255,255,255,440)
    lib_sl.speedfade(4,3,255,255,255,440)
    time.sleep(0.235)
    lib_sl.speedfade(5,2,255,255,255,440)
    lib_sl.speedfade(5,3,255,255,255,440)
    lib_sl.speedfade(6,3,255,255,255,440)
    lib_sl.speedfade(1,3,255,255,255,440)
    lib_sl.speedfade(2,2,255,255,255,440)
    lib_sl.speedfade(2,3,255,255,255,440)
    lib_sl.speedfade(6,2,255,255,255,440)
    lib_sl.speedfade(7,2,255,255,255,440)
    lib_sl.speedfade(7,3,255,255,255,440)
    lib_sl.speedfade(0,2,255,255,255,440)
    lib_sl.speedfade(0,3,255,255,255,440)
    lib_sl.speedfade(1,2,255,255,255,440)
    time.sleep(0.235)
    lib_sl.speedfade(6,0,255,255,255,440)
    lib_sl.speedfade(7,0,255,255,255,440)
    lib_sl.speedfade(7,1,255,255,255,440)
    lib_sl.speedfade(0,0,255,255,255,440)
    lib_sl.speedfade(0,1,255,255,255,440)
    lib_sl.speedfade(1,0,255,255,255,440)
    lib_sl.speedfade(5,4,255,255,255,440)
    lib_sl.speedfade(5,5,255,255,255,440)
    lib_sl.speedfade(6,4,255,255,255,440)
    lib_sl.speedfade(3,4,255,255,255,440)
    lib_sl.speedfade(3,5,255,255,255,440)
    lib_sl.speedfade(4,4,255,255,255,440)
    lib_sl.speedfade(4,5,255,255,255,440)
    lib_sl.speedfade(1,4,255,255,255,440)
    lib_sl.speedfade(2,4,255,255,255,440)
    lib_sl.speedfade(2,5,255,255,255,440)
    time.sleep(0.235)
    lib_sl.speedfade(5,0,255,255,255,440)
    lib_sl.speedfade(5,1,255,255,255,440)
    lib_sl.speedfade(6,1,255,255,255,440)
    lib_sl.speedfade(3,0,255,255,255,440)
    lib_sl.speedfade(3,1,255,255,255,440)
    lib_sl.speedfade(4,0,255,255,255,440)
    lib_sl.speedfade(4,1,255,255,255,440)
    lib_sl.speedfade(1,1,255,255,255,440)
    lib_sl.speedfade(2,0,255,255,255,440)
    lib_sl.speedfade(2,1,255,255,255,440)
    lib_sl.speedfade(7,4,255,255,255,440)
    lib_sl.speedfade(6,5,255,255,255,440)
    lib_sl.speedfade(7,5,255,255,255,440)
    lib_sl.speedfade(0,4,255,255,255,440)
    lib_sl.speedfade(0,5,255,255,255,440)
    lib_sl.speedfade(1,5,255,255,255,440)
    time.sleep(0.235)
    lib_sl.speedfade(1,3,0,0,255,440)
    lib_sl.speedfade(2,2,0,0,255,440)
    lib_sl.speedfade(2,3,0,0,255,440)
    lib_sl.speedfade(0,2,0,0,255,440)
    lib_sl.speedfade(0,3,0,0,255,440)
    lib_sl.speedfade(1,2,0,0,255,440)
    time.sleep(0.235)
    lib_sl.speedfade(3,2,0,0,255,440)
    lib_sl.speedfade(3,3,0,0,255,440)
    lib_sl.speedfade(4,2,0,0,255,440)
    lib_sl.speedfade(4,3,0,0,255,440)
    lib_sl.speedfade(0,0,0,0,255,440)
    lib_sl.speedfade(0,1,0,0,255,440)
    lib_sl.speedfade(1,0,0,0,255,440)
    lib_sl.speedfade(5,2,0,0,255,440)
    lib_sl.speedfade(5,3,0,0,255,440)
    lib_sl.speedfade(6,3,0,0,255,440)
    lib_sl.speedfade(6,2,0,0,255,440)
    lib_sl.speedfade(7,2,0,0,255,440)
    lib_sl.speedfade(7,3,0,0,255,440)
    lib_sl.speedfade(3,4,0,0,255,440)
    lib_sl.speedfade(3,5,0,0,255,440)
    lib_sl.speedfade(4,4,0,0,255,440)
    lib_sl.speedfade(4,5,0,0,255,440)
    lib_sl.speedfade(1,4,0,0,255,440)
    lib_sl.speedfade(2,4,0,0,255,440)
    lib_sl.speedfade(2,5,0,0,255,440)
    lib_sl.speedfade(1,3,136,136,221,320)
    lib_sl.speedfade(2,2,136,136,221,320)
    lib_sl.speedfade(2,3,136,136,221,320)
    lib_sl.speedfade(0,2,136,136,221,320)
    lib_sl.speedfade(0,3,136,136,221,320)
    lib_sl.speedfade(1,2,136,136,221,320)
    time.sleep(0.235)
    lib_sl.speedfade(1,1,0,0,255,440)
    lib_sl.speedfade(2,0,0,0,255,440)
    lib_sl.speedfade(2,1,0,0,255,440)
    lib_sl.speedfade(3,0,0,0,255,440)
    lib_sl.speedfade(3,1,0,0,255,440)
    lib_sl.speedfade(4,0,0,0,255,440)
    lib_sl.speedfade(4,1,0,0,255,440)
    lib_sl.speedfade(5,0,0,0,255,440)
    lib_sl.speedfade(5,1,0,0,255,440)
    lib_sl.speedfade(6,1,0,0,255,440)
    lib_sl.speedfade(6,0,0,0,255,440)
    lib_sl.speedfade(7,0,0,0,255,440)
    lib_sl.speedfade(7,1,0,0,255,440)
    lib_sl.speedfade(5,4,0,0,255,440)
    lib_sl.speedfade(5,5,0,0,255,440)
    lib_sl.speedfade(6,4,0,0,255,440)
    lib_sl.speedfade(7,4,0,0,255,440)
    lib_sl.speedfade(6,5,0,0,255,440)
    lib_sl.speedfade(7,5,0,0,255,440)
    lib_sl.speedfade(0,4,0,0,255,440)
    lib_sl.speedfade(0,5,0,0,255,440)
    lib_sl.speedfade(1,5,0,0,255,440)
    lib_sl.speedfade(0,0,136,136,221,320)
    lib_sl.speedfade(0,1,136,136,221,320)
    lib_sl.speedfade(1,0,136,136,221,320)
    lib_sl.speedfade(3,2,136,136,221,320)
    lib_sl.speedfade(3,3,136,136,221,320)
    lib_sl.speedfade(4,2,136,136,221,320)
    lib_sl.speedfade(4,3,136,136,221,320)
    lib_sl.speedfade(3,4,136,136,221,320)
    lib_sl.speedfade(3,5,136,136,221,320)
    lib_sl.speedfade(4,4,136,136,221,320)
    lib_sl.speedfade(4,5,136,136,221,320)
    lib_sl.speedfade(1,4,136,136,221,320)
    lib_sl.speedfade(2,4,136,136,221,320)
    lib_sl.speedfade(2,5,136,136,221,320)
    time.sleep(0.235)
    lib_sl.speedfade(1,1,136,136,221,320)
    lib_sl.speedfade(2,0,136,136,221,320)
    lib_sl.speedfade(2,1,136,136,221,320)
    lib_sl.speedfade(3,0,136,136,221,320)
    lib_sl.speedfade(3,1,136,136,221,320)
    lib_sl.speedfade(4,0,136,136,221,320)
    lib_sl.speedfade(4,1,136,136,221,320)
    lib_sl.speedfade(5,0,136,136,221,320)
    lib_sl.speedfade(5,1,136,136,221,320)
    lib_sl.speedfade(6,1,136,136,221,320)
    lib_sl.speedfade(6,0,136,136,221,320)
    lib_sl.speedfade(7,0,136,136,221,320)
    lib_sl.speedfade(7,1,136,136,221,320)
    lib_sl.speedfade(5,2,136,136,221,320)
    lib_sl.speedfade(5,3,136,136,221,320)
    lib_sl.speedfade(6,3,136,136,221,320)
    lib_sl.speedfade(6,2,136,136,221,320)
    lib_sl.speedfade(7,2,136,136,221,320)
    lib_sl.speedfade(7,3,136,136,221,320)
    lib_sl.speedfade(5,4,136,136,221,320)
    lib_sl.speedfade(5,5,136,136,221,320)
    lib_sl.speedfade(6,4,136,136,221,320)
    lib_sl.speedfade(7,4,136,136,221,320)
    lib_sl.speedfade(6,5,136,136,221,320)
    lib_sl.speedfade(7,5,136,136,221,320)
    lib_sl.speedfade(0,4,136,136,221,320)
    lib_sl.speedfade(0,5,136,136,221,320)
    lib_sl.speedfade(1,5,136,136,221,320)
    time.sleep(2.351)
    lib_sl.speedfade(0,0,255,255,255,880)
    lib_sl.speedfade(0,1,255,255,255,880)
    lib_sl.speedfade(0,2,255,255,255,880)
    lib_sl.speedfade(0,3,255,255,255,880)
    lib_sl.speedfade(0,4,255,255,255,880)
    lib_sl.speedfade(0,5,255,255,255,880)
    lib_sl.speedfade(1,0,255,255,255,880)
    lib_sl.speedfade(1,1,255,255,255,880)
    lib_sl.speedfade(1,2,255,255,255,880)
    lib_sl.speedfade(1,3,255,255,255,880)
    lib_sl.speedfade(1,4,255,255,255,880)
    lib_sl.speedfade(1,5,255,255,255,880)
    lib_sl.speedfade(2,0,255,255,255,880)
    lib_sl.speedfade(2,1,255,255,255,880)
    lib_sl.speedfade(2,2,255,255,255,880)
    lib_sl.speedfade(2,3,255,255,255,880)
    lib_sl.speedfade(2,4,255,255,255,880)
    lib_sl.speedfade(2,5,255,255,255,880)
    lib_sl.speedfade(3,0,255,255,255,880)
    lib_sl.speedfade(3,1,255,255,255,880)
    lib_sl.speedfade(3,2,255,255,255,880)
    lib_sl.speedfade(3,3,255,255,255,880)
    lib_sl.speedfade(3,4,255,255,255,880)
    lib_sl.speedfade(3,5,255,255,255,880)
    lib_sl.speedfade(4,0,255,255,255,880)
    lib_sl.speedfade(4,1,255,255,255,880)
    lib_sl.speedfade(4,2,255,255,255,880)
    lib_sl.speedfade(4,3,255,255,255,880)
    lib_sl.speedfade(4,4,255,255,255,880)
    lib_sl.speedfade(4,5,255,255,255,880)
    lib_sl.speedfade(5,0,255,255,255,880)
    lib_sl.speedfade(5,1,255,255,255,880)
    lib_sl.speedfade(5,2,255,255,255,880)
    lib_sl.speedfade(5,3,255,255,255,880)
    lib_sl.speedfade(5,4,255,255,255,880)
    lib_sl.speedfade(5,5,255,255,255,880)
    lib_sl.speedfade(6,0,255,255,255,880)
    lib_sl.speedfade(6,1,255,255,255,880)
    lib_sl.speedfade(6,2,255,255,255,880)
    lib_sl.speedfade(6,3,255,255,255,880)
    lib_sl.speedfade(6,4,255,255,255,880)
    lib_sl.speedfade(6,5,255,255,255,880)
    lib_sl.speedfade(7,0,255,255,255,880)
    lib_sl.speedfade(7,1,255,255,255,880)
    lib_sl.speedfade(7,2,255,255,255,880)
    lib_sl.speedfade(7,3,255,255,255,880)
    lib_sl.speedfade(7,4,255,255,255,880)
    lib_sl.speedfade(7,5,255,255,255,880)
    time.sleep(0.235)
    lib_sl.speedfade(0,0,136,136,221,235)
    lib_sl.speedfade(0,1,136,136,221,235)
    lib_sl.speedfade(0,2,136,136,221,235)
    lib_sl.speedfade(0,3,136,136,221,235)
    lib_sl.speedfade(0,4,136,136,221,235)
    lib_sl.speedfade(0,5,136,136,221,235)
    lib_sl.speedfade(1,0,136,136,221,235)
    lib_sl.speedfade(1,1,136,136,221,235)
    lib_sl.speedfade(1,2,136,136,221,235)
    lib_sl.speedfade(1,3,136,136,221,235)
    lib_sl.speedfade(1,4,136,136,221,235)
    lib_sl.speedfade(1,5,136,136,221,235)
    lib_sl.speedfade(2,0,136,136,221,235)
    lib_sl.speedfade(2,1,136,136,221,235)
    lib_sl.speedfade(2,2,136,136,221,235)
    lib_sl.speedfade(2,3,136,136,221,235)
    lib_sl.speedfade(2,4,136,136,221,235)
    lib_sl.speedfade(2,5,136,136,221,235)
    lib_sl.speedfade(3,0,136,136,221,235)
    lib_sl.speedfade(3,1,136,136,221,235)
    lib_sl.speedfade(3,2,136,136,221,235)
    lib_sl.speedfade(3,3,136,136,221,235)
    lib_sl.speedfade(3,4,136,136,221,235)
    lib_sl.speedfade(3,5,136,136,221,235)
    lib_sl.speedfade(4,0,136,136,221,235)
    lib_sl.speedfade(4,1,136,136,221,235)
    lib_sl.speedfade(4,2,136,136,221,235)
    lib_sl.speedfade(4,3,136,136,221,235)
    lib_sl.speedfade(4,4,136,136,221,235)
    lib_sl.speedfade(4,5,136,136,221,235)
    lib_sl.speedfade(5,0,136,136,221,235)
    lib_sl.speedfade(5,1,136,136,221,235)
    lib_sl.speedfade(5,2,136,136,221,235)
    lib_sl.speedfade(5,3,136,136,221,235)
    lib_sl.speedfade(5,4,136,136,221,235)
    lib_sl.speedfade(5,5,136,136,221,235)
    lib_sl.speedfade(6,0,136,136,221,235)
    lib_sl.speedfade(6,1,136,136,221,235)
    lib_sl.speedfade(6,2,136,136,221,235)
    lib_sl.speedfade(6,3,136,136,221,235)
    lib_sl.speedfade(6,4,136,136,221,235)
    lib_sl.speedfade(6,5,136,136,221,235)
    lib_sl.speedfade(7,0,136,136,221,235)
    lib_sl.speedfade(7,1,136,136,221,235)
    lib_sl.speedfade(7,2,136,136,221,235)
    lib_sl.speedfade(7,3,136,136,221,235)
    lib_sl.speedfade(7,4,136,136,221,235)
    lib_sl.speedfade(7,5,136,136,221,235)
    time.sleep(0.235)
    lib_sl.speedfade(0,0,255,255,255,880)
    lib_sl.speedfade(0,1,255,255,255,880)
    lib_sl.speedfade(0,2,255,255,255,880)
    lib_sl.speedfade(0,3,255,255,255,880)
    lib_sl.speedfade(0,4,255,255,255,880)
    lib_sl.speedfade(0,5,255,255,255,880)
    lib_sl.speedfade(1,0,255,255,255,880)
    lib_sl.speedfade(1,1,255,255,255,880)
    lib_sl.speedfade(1,2,255,255,255,880)
    lib_sl.speedfade(1,3,255,255,255,880)
    lib_sl.speedfade(1,4,255,255,255,880)
    lib_sl.speedfade(1,5,255,255,255,880)
    lib_sl.speedfade(2,0,255,255,255,880)
    lib_sl.speedfade(2,1,255,255,255,880)
    lib_sl.speedfade(2,2,255,255,255,880)
    lib_sl.speedfade(2,3,255,255,255,880)
    lib_sl.speedfade(2,4,255,255,255,880)
    lib_sl.speedfade(2,5,255,255,255,880)
    lib_sl.speedfade(3,0,255,255,255,880)
    lib_sl.speedfade(3,1,255,255,255,880)
    lib_sl.speedfade(3,2,255,255,255,880)
    lib_sl.speedfade(3,3,255,255,255,880)
    lib_sl.speedfade(3,4,255,255,255,880)
    lib_sl.speedfade(3,5,255,255,255,880)
    lib_sl.speedfade(4,0,255,255,255,880)
    lib_sl.speedfade(4,1,255,255,255,880)
    lib_sl.speedfade(4,2,255,255,255,880)
    lib_sl.speedfade(4,3,255,255,255,880)
    lib_sl.speedfade(4,4,255,255,255,880)
    lib_sl.speedfade(4,5,255,255,255,880)
    lib_sl.speedfade(5,0,255,255,255,880)
    lib_sl.speedfade(5,1,255,255,255,880)
    lib_sl.speedfade(5,2,255,255,255,880)
    lib_sl.speedfade(5,3,255,255,255,880)
    lib_sl.speedfade(5,4,255,255,255,880)
    lib_sl.speedfade(5,5,255,255,255,880)
    lib_sl.speedfade(6,0,255,255,255,880)
    lib_sl.speedfade(6,1,255,255,255,880)
    lib_sl.speedfade(6,2,255,255,255,880)
    lib_sl.speedfade(6,3,255,255,255,880)
    lib_sl.speedfade(6,4,255,255,255,880)
    lib_sl.speedfade(6,5,255,255,255,880)
    lib_sl.speedfade(7,0,255,255,255,880)
    lib_sl.speedfade(7,1,255,255,255,880)
    lib_sl.speedfade(7,2,255,255,255,880)
    lib_sl.speedfade(7,3,255,255,255,880)
    lib_sl.speedfade(7,4,255,255,255,880)
    lib_sl.speedfade(7,5,255,255,255,880)
    time.sleep(0.235)
    lib_sl.speedfade(0,0,136,136,221,235)
    lib_sl.speedfade(0,1,136,136,221,235)
    lib_sl.speedfade(0,2,136,136,221,235)
    lib_sl.speedfade(0,3,136,136,221,235)
    lib_sl.speedfade(0,4,136,136,221,235)
    lib_sl.speedfade(0,5,136,136,221,235)
    lib_sl.speedfade(1,0,136,136,221,235)
    lib_sl.speedfade(1,1,136,136,221,235)
    lib_sl.speedfade(1,2,136,136,221,235)
    lib_sl.speedfade(1,3,136,136,221,235)
    lib_sl.speedfade(1,4,136,136,221,235)
    lib_sl.speedfade(1,5,136,136,221,235)
    lib_sl.speedfade(2,0,136,136,221,235)
    lib_sl.speedfade(2,1,136,136,221,235)
    lib_sl.speedfade(2,2,136,136,221,235)
    lib_sl.speedfade(2,3,136,136,221,235)
    lib_sl.speedfade(2,4,136,136,221,235)
    lib_sl.speedfade(2,5,136,136,221,235)
    lib_sl.speedfade(3,0,136,136,221,235)
    lib_sl.speedfade(3,1,136,136,221,235)
    lib_sl.speedfade(3,2,136,136,221,235)
    lib_sl.speedfade(3,3,136,136,221,235)
    lib_sl.speedfade(3,4,136,136,221,235)
    lib_sl.speedfade(3,5,136,136,221,235)
    lib_sl.speedfade(4,0,136,136,221,235)
    lib_sl.speedfade(4,1,136,136,221,235)
    lib_sl.speedfade(4,2,136,136,221,235)
    lib_sl.speedfade(4,3,136,136,221,235)
    lib_sl.speedfade(4,4,136,136,221,235)
    lib_sl.speedfade(4,5,136,136,221,235)
    lib_sl.speedfade(5,0,136,136,221,235)
    lib_sl.speedfade(5,1,136,136,221,235)
    lib_sl.speedfade(5,2,136,136,221,235)
    lib_sl.speedfade(5,3,136,136,221,235)
    lib_sl.speedfade(5,4,136,136,221,235)
    lib_sl.speedfade(5,5,136,136,221,235)
    lib_sl.speedfade(6,0,136,136,221,235)
    lib_sl.speedfade(6,1,136,136,221,235)
    lib_sl.speedfade(6,2,136,136,221,235)
    lib_sl.speedfade(6,3,136,136,221,235)
    lib_sl.speedfade(6,4,136,136,221,235)
    lib_sl.speedfade(6,5,136,136,221,235)
    lib_sl.speedfade(7,0,136,136,221,235)
    lib_sl.speedfade(7,1,136,136,221,235)
    lib_sl.speedfade(7,2,136,136,221,235)
    lib_sl.speedfade(7,3,136,136,221,235)
    lib_sl.speedfade(7,4,136,136,221,235)
    lib_sl.speedfade(7,5,136,136,221,235)
    time.sleep(1.111)
    lib_sl.speedfade(0,0,255,255,255,880)
    lib_sl.speedfade(0,1,255,255,255,880)
    lib_sl.speedfade(0,2,255,255,255,880)
    lib_sl.speedfade(0,3,255,255,255,880)
    lib_sl.speedfade(0,4,255,255,255,880)
    lib_sl.speedfade(0,5,255,255,255,880)
    lib_sl.speedfade(1,0,255,255,255,880)
    lib_sl.speedfade(1,1,255,255,255,880)
    lib_sl.speedfade(1,2,255,255,255,880)
    lib_sl.speedfade(1,3,255,255,255,880)
    lib_sl.speedfade(1,4,255,255,255,880)
    lib_sl.speedfade(1,5,255,255,255,880)
    lib_sl.speedfade(2,0,255,255,255,880)
    lib_sl.speedfade(2,1,255,255,255,880)
    lib_sl.speedfade(2,2,255,255,255,880)
    lib_sl.speedfade(2,3,255,255,255,880)
    lib_sl.speedfade(2,4,255,255,255,880)
    lib_sl.speedfade(2,5,255,255,255,880)
    lib_sl.speedfade(3,0,255,255,255,880)
    lib_sl.speedfade(3,1,255,255,255,880)
    lib_sl.speedfade(3,2,255,255,255,880)
    lib_sl.speedfade(3,3,255,255,255,880)
    lib_sl.speedfade(3,4,255,255,255,880)
    lib_sl.speedfade(3,5,255,255,255,880)
    lib_sl.speedfade(4,0,255,255,255,880)
    lib_sl.speedfade(4,1,255,255,255,880)
    lib_sl.speedfade(4,2,255,255,255,880)
    lib_sl.speedfade(4,3,255,255,255,880)
    lib_sl.speedfade(4,4,255,255,255,880)
    lib_sl.speedfade(4,5,255,255,255,880)
    lib_sl.speedfade(5,0,255,255,255,880)
    lib_sl.speedfade(5,1,255,255,255,880)
    lib_sl.speedfade(5,2,255,255,255,880)
    lib_sl.speedfade(5,3,255,255,255,880)
    lib_sl.speedfade(5,4,255,255,255,880)
    lib_sl.speedfade(5,5,255,255,255,880)
    lib_sl.speedfade(6,0,255,255,255,880)
    lib_sl.speedfade(6,1,255,255,255,880)
    lib_sl.speedfade(6,2,255,255,255,880)
    lib_sl.speedfade(6,3,255,255,255,880)
    lib_sl.speedfade(6,4,255,255,255,880)
    lib_sl.speedfade(6,5,255,255,255,880)
    lib_sl.speedfade(7,0,255,255,255,880)
    lib_sl.speedfade(7,1,255,255,255,880)
    lib_sl.speedfade(7,2,255,255,255,880)
    lib_sl.speedfade(7,3,255,255,255,880)
    lib_sl.speedfade(7,4,255,255,255,880)
    lib_sl.speedfade(7,5,255,255,255,880)
    time.sleep(0.235)
    lib_sl.speedfade(0,0,136,136,221,235)
    lib_sl.speedfade(0,1,136,136,221,235)
    lib_sl.speedfade(0,2,136,136,221,235)
    lib_sl.speedfade(0,3,136,136,221,235)
    lib_sl.speedfade(0,4,136,136,221,235)
    lib_sl.speedfade(0,5,136,136,221,235)
    lib_sl.speedfade(1,0,136,136,221,235)
    lib_sl.speedfade(1,1,136,136,221,235)
    lib_sl.speedfade(1,2,136,136,221,235)
    lib_sl.speedfade(1,3,136,136,221,235)
    lib_sl.speedfade(1,4,136,136,221,235)
    lib_sl.speedfade(1,5,136,136,221,235)
    lib_sl.speedfade(2,0,136,136,221,235)
    lib_sl.speedfade(2,1,136,136,221,235)
    lib_sl.speedfade(2,2,136,136,221,235)
    lib_sl.speedfade(2,3,136,136,221,235)
    lib_sl.speedfade(2,4,136,136,221,235)
    lib_sl.speedfade(2,5,136,136,221,235)
    lib_sl.speedfade(3,0,136,136,221,235)
    lib_sl.speedfade(3,1,136,136,221,235)
    lib_sl.speedfade(3,2,136,136,221,235)
    lib_sl.speedfade(3,3,136,136,221,235)
    lib_sl.speedfade(3,4,136,136,221,235)
    lib_sl.speedfade(3,5,136,136,221,235)
    lib_sl.speedfade(4,0,136,136,221,235)
    lib_sl.speedfade(4,1,136,136,221,235)
    lib_sl.speedfade(4,2,136,136,221,235)
    lib_sl.speedfade(4,3,136,136,221,235)
    lib_sl.speedfade(4,4,136,136,221,235)
    lib_sl.speedfade(4,5,136,136,221,235)
    lib_sl.speedfade(5,0,136,136,221,235)
    lib_sl.speedfade(5,1,136,136,221,235)
    lib_sl.speedfade(5,2,136,136,221,235)
    lib_sl.speedfade(5,3,136,136,221,235)
    lib_sl.speedfade(5,4,136,136,221,235)
    lib_sl.speedfade(5,5,136,136,221,235)
    lib_sl.speedfade(6,0,136,136,221,235)
    lib_sl.speedfade(6,1,136,136,221,235)
    lib_sl.speedfade(6,2,136,136,221,235)
    lib_sl.speedfade(6,3,136,136,221,235)
    lib_sl.speedfade(6,4,136,136,221,235)
    lib_sl.speedfade(6,5,136,136,221,235)
    lib_sl.speedfade(7,0,136,136,221,235)
    lib_sl.speedfade(7,1,136,136,221,235)
    lib_sl.speedfade(7,2,136,136,221,235)
    lib_sl.speedfade(7,3,136,136,221,235)
    lib_sl.speedfade(7,4,136,136,221,235)
    lib_sl.speedfade(7,5,136,136,221,235)
    time.sleep(1.234)
    lib_sl.speedfade(3,2,255,255,255,880)
    lib_sl.speedfade(3,3,255,255,255,880)
    lib_sl.speedfade(4,2,255,255,255,880)
    lib_sl.speedfade(4,3,255,255,255,880)
    lib_sl.speedfade(3,0,255,255,255,880)
    lib_sl.speedfade(3,1,255,255,255,880)
    lib_sl.speedfade(4,0,255,255,255,880)
    lib_sl.speedfade(4,1,255,255,255,880)
    lib_sl.speedfade(3,4,255,255,255,880)
    lib_sl.speedfade(3,5,255,255,255,880)
    lib_sl.speedfade(4,4,255,255,255,880)
    lib_sl.speedfade(4,5,255,255,255,880)
    time.sleep(2.351)
