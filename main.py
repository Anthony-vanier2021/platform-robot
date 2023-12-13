#Remote Hello World - Turns West Motor
import config, time
from machine import Pin, PWM

ms1 = Pin(config.MS1_PINNUM, mode=Pin.OUT, value=0)
ms2 = Pin(config.MS2_PINNUM, mode=Pin.OUT, value=0)
ms3 = Pin(config.MS3_PINNUM, mode=Pin.OUT, value=0)
step = PWM(Pin(config.STEP_PINNUM, mode=Pin.OUT))
rsth = Pin(config.RSTH_PINNUM, mode=Pin.OUT, value=1)
slph = Pin(config.SLPH_PINNUM, mode=Pin.OUT, value=1)
dir1 = Pin(config.DIR1_PINNUM, mode=Pin.OUT, value=0)
step.freq(1_000)    #1KHz frequency


for i in range(10):
    step.duty(512)
    time.sleep_ms(500)
    step.duty(0)
    dir1.value(1)
    step.duty(512)
    time.sleep_ms(500)
    step.duty(0)
