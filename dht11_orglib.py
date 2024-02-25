import RPi.GPIO as GPIO
import time

# Initialization of dht11
def init_dht11(SelectPin):
    GPIO.setmode(SelectPin, GPIO.OUT)
    GPIO.output(SelectPin, GPIO.HIGH)
    delay_time(0.5)
    GPIO.output(SelectPin, GPIO.LOW)
    delay_time(0.02)
    GPIO.output(SelectPin, GPIO.HIGH)
    GPIO.setmode(SelectPin, GPIO.IN)

# Read data from dht11
def data_get(SelectPin):
    Pulse_cnt = 0
    level = GPIO.input(SelectPin)

    # Detect LOW
    while level == 0:
        Pulse_cnt += 5
        delay_time(0.000005)
        level = GPIO.input(SelectPin)

    # Detect HIGH
    while level == 1:
        Pulse_cnt += 5
        delay_time(0.000005)
        level = GPIO.input(SelectPin)

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
def checksum(Data):
    print("checksum")

# Binary to decimal conversion
def convert(SourceData, GenerateData):
    for i in range(5):
        GenerateData[i] = int(''.join(map(str, SourceData[i*8:(i+1)*8])), 2)

# Stops program for requested time (depends on system time)
def delay_time(DelayTime):
    StartTime = time.monotonic()
    ElapsedTime = 0
    while ElapsedTime < DelayTime:
        ElapsedTime = time.monotonic() - StartTime
