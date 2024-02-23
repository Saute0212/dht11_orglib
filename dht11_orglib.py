import RPi.GPIO as GPIO
import time

# Parameter
DATA_PIN=17

# Initialization of dht11
def init_dht11():
    GPIO.setmode(DATA_PIN, GPIO.OUT)
    GPIO.output(DATA_PIN, GPIO.HIGH)
    delay_time(0.5)
    GPIO.output(DATA_PIN, GPIO.LOW)
    delay_time(0.02)
    GPIO.output(DATA_PIN, GPIO.HIGH)
    GPIO.setmode(DATA_PIN, GPIO.IN)
    
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
