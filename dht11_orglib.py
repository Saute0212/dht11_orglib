import RPi.GPIO as GPIO
import time

# Parameter
DATA_PIN=17

# Variables

# Initialization of dht11
def init_dht11():
    GPIO.setmode(DATA_PIN, GPIO.OUT)
    GPIO.output(DATA_PIN, GPIO.HIGH)
    delay_time(0.5)
    GPIO.output(DATA_PIN, GPIO.LOW)
    delay_time(0.02)
    GPIO.output(DATA_PIN, GPIO.HIGH)
    GPIO.setmode(DATA_PIN, GPIO.IN)

# Read data from dht11
def data_get():
    Pulse_cnt = 0
    level = GPIO.input(DATA_PIN)

    # Detect LOW
    while level == 0:
        Pulse_cnt += 5
        delay_time(0.000005)
        level = GPIO.input(DATA_PIN)

    # Detect HIGH
    while level == 1:
        Pulse_cnt += 5
        delay_time(0.000005)
        level = GPIO.input(DATA_PIN)

    # Error : ±10%
    if 70 < Pulse_cnt < 90:
        # Data : 0
        return 0
    elif 105 < Pulse_cnt < 135:
        # Data : 1
        return 1
    elif 140 < Pulse_cnt < 180:
        # Data : Ready
        return 2
    else:
        # Error
        return 3

# Detect an error
def checksum():
    print("checksum")

# Binary to decimal conversion
def convert():
    print("convert")

# Stops program for requested time (depends on system time)
def delay_time(DelayTime):
    StartTime = time.monotonic()
    ElapsedTime = 0
    while ElapsedTime < DelayTime:
        ElapsedTime = time.monotonic() - StartTime
