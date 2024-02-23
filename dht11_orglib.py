import pigpio
import time

# Parameter
DATA_PIN=17

pi = pigpio.pi()

# Initialization of dht11
def init_dht11():
    pi.set_mode(DATA_PIN, pigpio.OUTPUT)
    pi.write(DATA_PIN, 1)
    delay_time(0.5)
    pi.write(DATA_PIN, 0)
    delay_time(0.02)
    pi.write(DATA_PIN, 1)
    pi.set_mode(DATA_PIN, pigpio.INPUT)
    
# Detect an error
def checksum():
    print("checksum")

# Read data from dht11
def bits_get():
    print("bits_get")

# Binary to decimal conversion
def convert():
    print("convert")

# Stops program for requested time (depends on system time)
def delay_time(DelayTime):
    StartTime = time.monotonic()
    ElapsedTime = 0
    while ElapsedTime < DelayTime:
        ElapsedTime = time.monotonic() - StartTime
