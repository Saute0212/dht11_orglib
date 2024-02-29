import time
import pigpio

PIN = 17

pi = pigpio.pi()

def delay_time(DelayTime):
    StartTime = time.monotonic()
    ElapsedTime = 0
    while ElapsedTime < DelayTime:
        ElapsedTime = time.monotonic() - StartTime

def init(pin):
    pi.set_mode(pin, pigpio.OUTPUT)
    pi.write(pin, 1)
    delay_time(0.5)
    pi.write(pin, 0)
    delay_time(0.02)
    pi.write(pin, 1)
    delay_time(0.01)
    pi.set_mode(pin, pigpio.INPUT)

    while True:
        if pi.read(pin) == 0:
            break
    while True:
        if pi.read(pin) == 1:
            break
    while True:
        if pi.read(pin) == 0:
            break
    return 1

while True:
    print(init(PIN))
