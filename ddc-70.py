# 70
import lib_sl
import random
import time

cs = [[255,255,000,000,000,255],[000,255,255,255,000,000],[000,000,000,255,255,255]]

def rc():
  return random.randint(0,5)

def rid():
    return [random.randint(0,8),random.randint(0,6)]


while 1:
#SEE HTTP://EN.WIKIPEDIA.ORG#/WIKI/GREEN_FLASH
    lib_sl.send(0,0,104,130,165)
    lib_sl.send(0,1,104,130,165)
    lib_sl.send(0,2,104,130,165)
    lib_sl.send(0,3,104,130,165)
    lib_sl.send(0,4,104,130,165)
    lib_sl.send(0,5,104,130,165)
    lib_sl.send(1,0,104,130,165)
    lib_sl.send(1,1,104,130,165)
    lib_sl.send(1,2,104,130,165)
    lib_sl.send(1,3,104,130,165)
    lib_sl.send(1,4,104,130,165)
    lib_sl.send(1,5,104,130,165)
    lib_sl.send(2,0,104,130,165)
    lib_sl.send(2,1,104,130,165)
    lib_sl.send(2,2,104,130,165)
    lib_sl.send(2,3,104,130,165)
    lib_sl.send(2,4,104,130,165)
    lib_sl.send(2,5,104,130,165)
    lib_sl.send(3,0,104,130,165)
    lib_sl.send(3,1,104,130,165)
    lib_sl.send(3,2,104,130,165)
    lib_sl.send(3,3,104,130,165)
    lib_sl.send(3,4,104,130,165)
    lib_sl.send(3,5,104,130,165)
    lib_sl.send(4,0,104,130,165)
    lib_sl.send(4,1,104,130,165)
    lib_sl.send(4,2,104,130,165)
    lib_sl.send(4,3,104,130,165)
    lib_sl.send(4,4,104,130,165)
    lib_sl.send(4,5,104,130,165)
    lib_sl.send(5,0,104,130,165)
    lib_sl.send(5,1,104,130,165)
    lib_sl.send(5,2,104,130,165)
    lib_sl.send(5,3,104,130,165)
    lib_sl.send(5,4,104,130,165)
    lib_sl.send(5,5,104,130,165)
    lib_sl.send(6,0,104,130,165)
    lib_sl.send(6,1,104,130,165)
    lib_sl.send(6,2,104,130,165)
    lib_sl.send(6,3,104,130,165)
    lib_sl.send(6,4,104,130,165)
    lib_sl.send(6,5,104,130,165)
    lib_sl.send(7,0,104,130,165)
    lib_sl.send(7,1,104,130,165)
    lib_sl.send(7,2,104,130,165)
    lib_sl.send(7,3,104,130,165)
    lib_sl.send(7,4,104,130,165)
    lib_sl.send(7,5,104,130,165)
    lib_sl.speedfade(0,0,255,149,84,80)
    lib_sl.speedfade(0,1,255,149,84,80)
    lib_sl.speedfade(0,2,255,149,84,80)
    lib_sl.speedfade(0,3,255,149,84,80)
    lib_sl.speedfade(0,4,255,149,84,80)
    lib_sl.speedfade(0,5,255,149,84,80)
    lib_sl.speedfade(1,0,255,149,84,80)
    lib_sl.speedfade(1,1,255,149,84,80)
    lib_sl.speedfade(1,2,255,149,84,80)
    lib_sl.speedfade(1,3,255,149,84,80)
    lib_sl.speedfade(1,4,255,149,84,80)
    lib_sl.speedfade(1,5,255,149,84,80)
    lib_sl.speedfade(2,0,255,149,84,80)
    lib_sl.speedfade(2,1,255,149,84,80)
    lib_sl.speedfade(2,2,255,149,84,80)
    lib_sl.speedfade(2,3,255,149,84,80)
    lib_sl.speedfade(2,4,255,149,84,80)
    lib_sl.speedfade(2,5,255,149,84,80)
    lib_sl.speedfade(3,0,255,149,84,80)
    lib_sl.speedfade(3,1,255,149,84,80)
    lib_sl.speedfade(3,2,255,149,84,80)
    lib_sl.speedfade(3,3,255,149,84,80)
    lib_sl.speedfade(3,4,255,149,84,80)
    lib_sl.speedfade(3,5,255,149,84,80)
    lib_sl.speedfade(4,0,255,149,84,80)
    lib_sl.speedfade(4,1,255,149,84,80)
    lib_sl.speedfade(4,2,255,149,84,80)
    lib_sl.speedfade(4,3,255,149,84,80)
    lib_sl.speedfade(4,4,255,149,84,80)
    lib_sl.speedfade(4,5,255,149,84,80)
    lib_sl.speedfade(5,0,255,149,84,80)
    lib_sl.speedfade(5,1,255,149,84,80)
    lib_sl.speedfade(5,2,255,149,84,80)
    lib_sl.speedfade(5,3,255,149,84,80)
    lib_sl.speedfade(5,4,255,149,84,80)
    lib_sl.speedfade(5,5,255,149,84,80)
    lib_sl.speedfade(6,0,255,149,84,80)
    lib_sl.speedfade(6,1,255,149,84,80)
    lib_sl.speedfade(6,2,255,149,84,80)
    lib_sl.speedfade(6,3,255,149,84,80)
    lib_sl.speedfade(6,4,255,149,84,80)
    lib_sl.speedfade(6,5,255,149,84,80)
    lib_sl.speedfade(7,0,255,149,84,80)
    lib_sl.speedfade(7,1,255,149,84,80)
    lib_sl.speedfade(7,2,255,149,84,80)
    lib_sl.speedfade(7,3,255,149,84,80)
    lib_sl.speedfade(7,4,255,149,84,80)
    lib_sl.speedfade(7,5,255,149,84,80)
    time.sleep(3.0)
    lib_sl.speedfade(0,0,157,19,19,46)
    lib_sl.speedfade(0,1,157,19,19,46)
    lib_sl.speedfade(0,2,157,19,19,46)
    lib_sl.speedfade(0,3,157,19,19,46)
    lib_sl.speedfade(0,4,157,19,19,46)
    lib_sl.speedfade(0,5,157,19,19,46)
    lib_sl.speedfade(1,0,157,19,19,46)
    lib_sl.speedfade(1,1,157,19,19,46)
    lib_sl.speedfade(1,2,157,19,19,46)
    lib_sl.speedfade(1,3,157,19,19,46)
    lib_sl.speedfade(1,4,157,19,19,46)
    lib_sl.speedfade(1,5,157,19,19,46)
    lib_sl.speedfade(2,0,157,19,19,46)
    lib_sl.speedfade(2,1,157,19,19,46)
    lib_sl.speedfade(2,2,157,19,19,46)
    lib_sl.speedfade(2,3,157,19,19,46)
    lib_sl.speedfade(2,4,157,19,19,46)
    lib_sl.speedfade(2,5,157,19,19,46)
    lib_sl.speedfade(3,0,157,19,19,46)
    lib_sl.speedfade(3,1,157,19,19,46)
    lib_sl.speedfade(3,2,157,19,19,46)
    lib_sl.speedfade(3,3,157,19,19,46)
    lib_sl.speedfade(3,4,157,19,19,46)
    lib_sl.speedfade(3,5,157,19,19,46)
    lib_sl.speedfade(4,0,157,19,19,46)
    lib_sl.speedfade(4,1,157,19,19,46)
    lib_sl.speedfade(4,2,157,19,19,46)
    lib_sl.speedfade(4,3,157,19,19,46)
    lib_sl.speedfade(4,4,157,19,19,46)
    lib_sl.speedfade(4,5,157,19,19,46)
    lib_sl.speedfade(5,0,157,19,19,46)
    lib_sl.speedfade(5,1,157,19,19,46)
    lib_sl.speedfade(5,2,157,19,19,46)
    lib_sl.speedfade(5,3,157,19,19,46)
    lib_sl.speedfade(5,4,157,19,19,46)
    lib_sl.speedfade(5,5,157,19,19,46)
    lib_sl.speedfade(6,0,157,19,19,46)
    lib_sl.speedfade(6,1,157,19,19,46)
    lib_sl.speedfade(6,2,157,19,19,46)
    lib_sl.speedfade(6,3,157,19,19,46)
    lib_sl.speedfade(6,4,157,19,19,46)
    lib_sl.speedfade(6,5,157,19,19,46)
    lib_sl.speedfade(7,0,157,19,19,46)
    lib_sl.speedfade(7,1,157,19,19,46)
    lib_sl.speedfade(7,2,157,19,19,46)
    lib_sl.speedfade(7,3,157,19,19,46)
    lib_sl.speedfade(7,4,157,19,19,46)
    lib_sl.speedfade(7,5,157,19,19,46)
    time.sleep(5.0)
    lib_sl.speedfade(0,0,0,255,0,309)
    lib_sl.speedfade(0,1,0,255,0,309)
    lib_sl.speedfade(0,2,0,255,0,309)
    lib_sl.speedfade(0,3,0,255,0,309)
    lib_sl.speedfade(0,4,0,255,0,309)
    lib_sl.speedfade(0,5,0,255,0,309)
    lib_sl.speedfade(1,0,0,255,0,309)
    lib_sl.speedfade(1,1,0,255,0,309)
    lib_sl.speedfade(1,2,0,255,0,309)
    lib_sl.speedfade(1,3,0,255,0,309)
    lib_sl.speedfade(1,4,0,255,0,309)
    lib_sl.speedfade(1,5,0,255,0,309)
    lib_sl.speedfade(2,0,0,255,0,309)
    lib_sl.speedfade(2,1,0,255,0,309)
    lib_sl.speedfade(2,2,0,255,0,309)
    lib_sl.speedfade(2,3,0,255,0,309)
    lib_sl.speedfade(2,4,0,255,0,309)
    lib_sl.speedfade(2,5,0,255,0,309)
    lib_sl.speedfade(3,0,0,255,0,309)
    lib_sl.speedfade(3,1,0,255,0,309)
    lib_sl.speedfade(3,2,0,255,0,309)
    lib_sl.speedfade(3,3,0,255,0,309)
    lib_sl.speedfade(3,4,0,255,0,309)
    lib_sl.speedfade(3,5,0,255,0,309)
    lib_sl.speedfade(4,0,0,255,0,309)
    lib_sl.speedfade(4,1,0,255,0,309)
    lib_sl.speedfade(4,2,0,255,0,309)
    lib_sl.speedfade(4,3,0,255,0,309)
    lib_sl.speedfade(4,4,0,255,0,309)
    lib_sl.speedfade(4,5,0,255,0,309)
    lib_sl.speedfade(5,0,0,255,0,309)
    lib_sl.speedfade(5,1,0,255,0,309)
    lib_sl.speedfade(5,2,0,255,0,309)
    lib_sl.speedfade(5,3,0,255,0,309)
    lib_sl.speedfade(5,4,0,255,0,309)
    lib_sl.speedfade(5,5,0,255,0,309)
    lib_sl.speedfade(6,0,0,255,0,309)
    lib_sl.speedfade(6,1,0,255,0,309)
    lib_sl.speedfade(6,2,0,255,0,309)
    lib_sl.speedfade(6,3,0,255,0,309)
    lib_sl.speedfade(6,4,0,255,0,309)
    lib_sl.speedfade(6,5,0,255,0,309)
    lib_sl.speedfade(7,0,0,255,0,309)
    lib_sl.speedfade(7,1,0,255,0,309)
    lib_sl.speedfade(7,2,0,255,0,309)
    lib_sl.speedfade(7,3,0,255,0,309)
    lib_sl.speedfade(7,4,0,255,0,309)
    lib_sl.speedfade(7,5,0,255,0,309)
    time.sleep(0.05)
