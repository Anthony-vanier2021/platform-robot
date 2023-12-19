#Remote Hello World - Should Turn East Motor, but doesn't work
import config, time
from machine import Pin, PWM

print("Setting Pins")
ms1 = Pin(config.MS1_PINNUM, mode=Pin.OUT, value=0)
ms2 = Pin(config.MS2_PINNUM, mode=Pin.OUT, value=0)
ms3 = Pin(config.MS3_PINNUM, mode=Pin.OUT, value=0)
step = Pin(config.STEP_PINNUM, mode=Pin.OUT)
rst = Pin(config.RSTH_PINNUM, mode=Pin.OUT, value=1)
slp = Pin(config.SLPH_PINNUM, mode=Pin.OUT, value=1)
dir = Pin(config.DIR2_PINNUM, mode=Pin.OUT, value=1)
#print("Setting frequency to 10Hz")
#step.freq(10)    #10Hz frequency
    #time.sleep_us(500)

num_step = 1000
dir.value(0 if num_step > 0 else 1)
print("Entering loop")
for i in range(abs(num_step)):
    step.value(1)
    time.sleep_us(20)
    step.value(0)
    time.sleep_us(20000)

print("End")