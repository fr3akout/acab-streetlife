# 222
import lib_sl
import random
import time

cs = [[255,255,000,000,000,255],[000,255,255,255,000,000],[000,000,000,255,255,255]]

def rc():
  return random.randint(0,5)

def rid():
    return [random.randint(0,8),random.randint(0,6)]


while 1:
#
# C O N S O L E
#

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

# CURSOR BLINK D
    lib_sl.send(5,0,60,255,0)
    lib_sl.send(5,1,60,255,0)
    lib_sl.send(6,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    time.sleep(0.2)
    lib_sl.send(5,0,60,255,0)
    lib_sl.send(5,1,60,255,0)
    lib_sl.send(6,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    time.sleep(0.2)
    lib_sl.send(5,0,60,255,0)
    lib_sl.send(5,1,60,255,0)
    lib_sl.send(6,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    time.sleep(0.2)
    lib_sl.send(5,0,60,255,0)
    lib_sl.send(5,1,60,255,0)
    lib_sl.send(6,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    time.sleep(0.2)
    lib_sl.send(5,0,60,255,0)
    lib_sl.send(5,1,60,255,0)
    lib_sl.send(6,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(5,0,0,0,0)
    lib_sl.send(5,1,0,0,0)
    lib_sl.send(6,1,0,0,0)
    time.sleep(0.2)

# CURSOR BACK STAY
    lib_sl.send(5,0,0,51,0)
    lib_sl.send(5,1,0,51,0)
    lib_sl.send(6,1,0,51,0)

# CURSOR MOVE
    lib_sl.send(6,0,60,255,0)
    lib_sl.send(7,0,60,255,0)
    lib_sl.send(7,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(6,0,0,0,0)
    lib_sl.send(7,0,0,0,0)
    lib_sl.send(7,1,0,0,0)
    time.sleep(0.2)


# CURSOR BACK STAY
    lib_sl.send(6,0,0,51,0)
    lib_sl.send(7,0,0,51,0)
    lib_sl.send(7,1,0,51,0)

# CURSOR MOVE
    lib_sl.send(5,2,60,255,0)
    lib_sl.send(5,3,60,255,0)
    lib_sl.send(6,3,60,255,0)
    time.sleep(0.2)
    lib_sl.send(5,2,0,0,0)
    lib_sl.send(5,3,0,0,0)
    lib_sl.send(6,3,0,0,0)
    time.sleep(0.2)


# CURSOR BACK STAY
    lib_sl.send(5,2,0,51,0)
    lib_sl.send(5,3,0,51,0)
    lib_sl.send(6,3,0,51,0)

# CURSOR MOVE
    lib_sl.send(6,2,60,255,0)
    lib_sl.send(7,2,60,255,0)
    lib_sl.send(7,3,60,255,0)
    time.sleep(0.2)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    time.sleep(0.2)
    lib_sl.send(6,2,60,255,0)
    lib_sl.send(7,2,60,255,0)
    lib_sl.send(7,3,60,255,0)
    time.sleep(0.2)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    time.sleep(0.2)
    lib_sl.send(6,2,60,255,0)
    lib_sl.send(7,2,60,255,0)
    lib_sl.send(7,3,60,255,0)
    time.sleep(0.2)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)
    time.sleep(0.2)
    lib_sl.send(6,2,60,255,0)
    lib_sl.send(7,2,60,255,0)
    lib_sl.send(7,3,60,255,0)
    time.sleep(0.2)
    lib_sl.send(6,2,0,0,0)
    lib_sl.send(7,2,0,0,0)
    lib_sl.send(7,3,0,0,0)


# CURSOR BACK STAY
    lib_sl.send(6,2,0,51,0)
    lib_sl.send(7,2,0,51,0)
    lib_sl.send(7,3,0,51,0)

# CURSOR MOVE
    lib_sl.send(5,4,60,255,0)
    lib_sl.send(5,5,60,255,0)
    lib_sl.send(6,4,60,255,0)
    time.sleep(0.2)
    lib_sl.send(5,4,0,0,0)
    lib_sl.send(5,5,0,0,0)
    lib_sl.send(6,4,0,0,0)
    time.sleep(0.2)

# CURSOR BACK STAY
    lib_sl.send(5,4,0,51,0)
    lib_sl.send(5,5,0,51,0)
    lib_sl.send(6,4,0,51,0)

# CURSOR BLINK D
    lib_sl.send(7,4,60,255,0)
    lib_sl.send(6,5,60,255,0)
    lib_sl.send(7,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
    time.sleep(0.2)
    lib_sl.send(7,4,60,255,0)
    lib_sl.send(6,5,60,255,0)
    lib_sl.send(7,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
    time.sleep(0.2)
    lib_sl.send(7,4,60,255,0)
    lib_sl.send(6,5,60,255,0)
    lib_sl.send(7,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
    time.sleep(0.2)
    lib_sl.send(7,4,60,255,0)
    lib_sl.send(6,5,60,255,0)
    lib_sl.send(7,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
    time.sleep(0.2)
    lib_sl.send(7,4,60,255,0)
    lib_sl.send(6,5,60,255,0)
    lib_sl.send(7,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(7,4,0,0,0)
    lib_sl.send(6,5,0,0,0)
    lib_sl.send(7,5,0,0,0)
    time.sleep(0.2)


# CURSOR BACK STAY
    lib_sl.send(7,4,0,51,0)
    lib_sl.send(6,5,0,51,0)
    lib_sl.send(7,5,0,51,0)



# CURSOR MOVE
    lib_sl.send(3,0,60,255,0)
    lib_sl.send(3,1,60,255,0)
    lib_sl.send(4,0,60,255,0)
    lib_sl.send(4,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    time.sleep(0.2)
    lib_sl.send(3,0,60,255,0)
    lib_sl.send(3,1,60,255,0)
    lib_sl.send(4,0,60,255,0)
    lib_sl.send(4,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(3,0,0,0,0)
    lib_sl.send(3,1,0,0,0)
    lib_sl.send(4,0,0,0,0)
    lib_sl.send(4,1,0,0,0)
    time.sleep(0.2)

# CURSOR BACK STAY
    lib_sl.send(3,0,0,51,0)
    lib_sl.send(3,1,0,51,0)
    lib_sl.send(4,0,0,51,0)
    lib_sl.send(4,1,0,51,0)

# CURSOR MOVE
    lib_sl.send(3,2,60,255,0)
    lib_sl.send(3,3,60,255,0)
    lib_sl.send(4,2,60,255,0)
    lib_sl.send(4,3,60,255,0)
    time.sleep(0.2)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    time.sleep(0.2)
    lib_sl.send(3,2,60,255,0)
    lib_sl.send(3,3,60,255,0)
    lib_sl.send(4,2,60,255,0)
    lib_sl.send(4,3,60,255,0)
    time.sleep(0.2)
    lib_sl.send(3,2,0,0,0)
    lib_sl.send(3,3,0,0,0)
    lib_sl.send(4,2,0,0,0)
    lib_sl.send(4,3,0,0,0)
    time.sleep(0.2)

# CURSOR BACK STAY
    lib_sl.send(3,2,0,51,0)
    lib_sl.send(3,3,0,51,0)
    lib_sl.send(4,2,0,51,0)
    lib_sl.send(4,3,0,51,0)

# CURSOR MOVE
    lib_sl.send(3,4,60,255,0)
    lib_sl.send(3,5,60,255,0)
    lib_sl.send(4,4,60,255,0)
    lib_sl.send(4,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    time.sleep(0.2)
    lib_sl.send(3,4,60,255,0)
    lib_sl.send(3,5,60,255,0)
    lib_sl.send(4,4,60,255,0)
    lib_sl.send(4,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(3,4,0,0,0)
    lib_sl.send(3,5,0,0,0)
    lib_sl.send(4,4,0,0,0)
    lib_sl.send(4,5,0,0,0)
    time.sleep(0.2)

# CURSOR BACK STAY
    lib_sl.send(3,4,0,51,0)
    lib_sl.send(3,5,0,51,0)
    lib_sl.send(4,4,0,51,0)
    lib_sl.send(4,5,0,51,0)




# CURSOR BLINK D
    lib_sl.send(1,1,60,255,0)
    lib_sl.send(2,0,60,255,0)
    lib_sl.send(2,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    time.sleep(0.2)
    lib_sl.send(1,1,60,255,0)
    lib_sl.send(2,0,60,255,0)
    lib_sl.send(2,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    time.sleep(0.2)
    lib_sl.send(1,1,60,255,0)
    lib_sl.send(2,0,60,255,0)
    lib_sl.send(2,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    time.sleep(0.2)
    lib_sl.send(1,1,60,255,0)
    lib_sl.send(2,0,60,255,0)
    lib_sl.send(2,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    time.sleep(0.2)
    lib_sl.send(1,1,60,255,0)
    lib_sl.send(2,0,60,255,0)
    lib_sl.send(2,1,60,255,0)
    time.sleep(0.2)
    lib_sl.send(1,1,0,0,0)
    lib_sl.send(2,0,0,0,0)
    lib_sl.send(2,1,0,0,0)
    time.sleep(0.2)

# CURSOR BACK STAY
    lib_sl.send(1,1,0,51,0)
    lib_sl.send(2,0,0,51,0)
    lib_sl.send(2,1,0,51,0)

# CURSOR MOVE
    lib_sl.send(0,0,60,255,0)
    lib_sl.send(0,1,60,255,0)
    lib_sl.send(1,0,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,0,0,0,0)
    lib_sl.send(0,1,0,0,0)
    lib_sl.send(1,0,0,0,0)
    time.sleep(0.2)

# CURSOR BACK STAY
    lib_sl.send(0,0,0,51,0)
    lib_sl.send(0,1,0,51,0)
    lib_sl.send(1,0,0,51,0)

# CURSOR MOVE
    lib_sl.send(1,3,60,255,0)
    lib_sl.send(2,2,60,255,0)
    lib_sl.send(2,3,60,255,0)
    time.sleep(0.2)
    lib_sl.send(1,3,0,0,0)
    lib_sl.send(2,2,0,0,0)
    lib_sl.send(2,3,0,0,0)
    time.sleep(0.2)


# CURSOR BACK STAY
    lib_sl.send(1,3,0,51,0)
    lib_sl.send(2,2,0,51,0)
    lib_sl.send(2,3,0,51,0)

# CURSOR MOVE
    lib_sl.send(0,2,60,255,0)
    lib_sl.send(0,3,60,255,0)
    lib_sl.send(1,2,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    time.sleep(0.2)
    lib_sl.send(0,2,60,255,0)
    lib_sl.send(0,3,60,255,0)
    lib_sl.send(1,2,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    time.sleep(0.2)
    lib_sl.send(0,2,60,255,0)
    lib_sl.send(0,3,60,255,0)
    lib_sl.send(1,2,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)
    time.sleep(0.2)
    lib_sl.send(0,2,60,255,0)
    lib_sl.send(0,3,60,255,0)
    lib_sl.send(1,2,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,2,0,0,0)
    lib_sl.send(0,3,0,0,0)
    lib_sl.send(1,2,0,0,0)


# CURSOR BACK STAY
    lib_sl.send(0,2,0,51,0)
    lib_sl.send(0,3,0,51,0)
    lib_sl.send(1,2,0,51,0)

# CURSOR MOVE
    lib_sl.send(1,4,60,255,0)
    lib_sl.send(2,4,60,255,0)
    lib_sl.send(2,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(1,4,0,0,0)
    lib_sl.send(2,4,0,0,0)
    lib_sl.send(2,5,0,0,0)
    time.sleep(0.2)

# CURSOR BACK STAY
    lib_sl.send(1,4,0,51,0)
    lib_sl.send(2,4,0,51,0)
    lib_sl.send(2,5,0,51,0)

# CURSOR BLINK D
    lib_sl.send(0,4,60,255,0)
    lib_sl.send(0,5,60,255,0)
    lib_sl.send(1,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
    time.sleep(0.2)
    lib_sl.send(0,4,60,255,0)
    lib_sl.send(0,5,60,255,0)
    lib_sl.send(1,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
    time.sleep(0.2)
    lib_sl.send(0,4,60,255,0)
    lib_sl.send(0,5,60,255,0)
    lib_sl.send(1,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
    time.sleep(0.2)
    lib_sl.send(0,4,60,255,0)
    lib_sl.send(0,5,60,255,0)
    lib_sl.send(1,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
    time.sleep(0.2)
    lib_sl.send(0,4,60,255,0)
    lib_sl.send(0,5,60,255,0)
    lib_sl.send(1,5,60,255,0)
    time.sleep(0.2)
    lib_sl.send(0,4,0,0,0)
    lib_sl.send(0,5,0,0,0)
    lib_sl.send(1,5,0,0,0)
    time.sleep(0.2)


# CURSOR BACK STAY
    lib_sl.send(0,4,0,51,0)
    lib_sl.send(0,5,0,51,0)
    lib_sl.send(1,5,0,51,0)


    lib_sl.speedfade(0,0,0,156,255,300)
    lib_sl.speedfade(0,1,0,156,255,300)
    lib_sl.speedfade(0,2,0,156,255,300)
    lib_sl.speedfade(0,3,0,156,255,300)
    lib_sl.speedfade(0,4,0,156,255,300)
    lib_sl.speedfade(0,5,0,156,255,300)
    lib_sl.speedfade(1,0,0,156,255,300)
    lib_sl.speedfade(1,1,0,156,255,300)
    lib_sl.speedfade(1,2,0,156,255,300)
    lib_sl.speedfade(1,3,0,156,255,300)
    lib_sl.speedfade(1,4,0,156,255,300)
    lib_sl.speedfade(1,5,0,156,255,300)
    lib_sl.speedfade(2,0,0,156,255,300)
    lib_sl.speedfade(2,1,0,156,255,300)
    lib_sl.speedfade(2,2,0,156,255,300)
    lib_sl.speedfade(2,3,0,156,255,300)
    lib_sl.speedfade(2,4,0,156,255,300)
    lib_sl.speedfade(2,5,0,156,255,300)
    lib_sl.speedfade(3,0,0,156,255,300)
    lib_sl.speedfade(3,1,0,156,255,300)
    lib_sl.speedfade(3,2,0,156,255,300)
    lib_sl.speedfade(3,3,0,156,255,300)
    lib_sl.speedfade(3,4,0,156,255,300)
    lib_sl.speedfade(3,5,0,156,255,300)
    lib_sl.speedfade(4,0,0,156,255,300)
    lib_sl.speedfade(4,1,0,156,255,300)
    lib_sl.speedfade(4,2,0,156,255,300)
    lib_sl.speedfade(4,3,0,156,255,300)
    lib_sl.speedfade(4,4,0,156,255,300)
    lib_sl.speedfade(4,5,0,156,255,300)
    lib_sl.speedfade(5,0,0,156,255,300)
    lib_sl.speedfade(5,1,0,156,255,300)
    lib_sl.speedfade(5,2,0,156,255,300)
    lib_sl.speedfade(5,3,0,156,255,300)
    lib_sl.speedfade(5,4,0,156,255,300)
    lib_sl.speedfade(5,5,0,156,255,300)
    lib_sl.speedfade(6,0,0,156,255,300)
    lib_sl.speedfade(6,1,0,156,255,300)
    lib_sl.speedfade(6,2,0,156,255,300)
    lib_sl.speedfade(6,3,0,156,255,300)
    lib_sl.speedfade(6,4,0,156,255,300)
    lib_sl.speedfade(6,5,0,156,255,300)
    lib_sl.speedfade(7,0,0,156,255,300)
    lib_sl.speedfade(7,1,0,156,255,300)
    lib_sl.speedfade(7,2,0,156,255,300)
    lib_sl.speedfade(7,3,0,156,255,300)
    lib_sl.speedfade(7,4,0,156,255,300)
    lib_sl.speedfade(7,5,0,156,255,300)
    time.sleep(3.0)
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
    time.sleep(0.1)


