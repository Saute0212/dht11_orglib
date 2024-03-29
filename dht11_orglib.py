import RPi.GPIO as GPIO
import time

# Initialization of dht11
def init_dht11(SelectPin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SelectPin, GPIO.OUT)
    GPIO.output(SelectPin, GPIO.HIGH)
    delay_time(0.5)
    GPIO.output(SelectPin, GPIO.LOW)
    delay_time(0.02)
    GPIO.output(SelectPin, GPIO.HIGH)
    GPIO.setup(SelectPin, GPIO.IN)
    # while data_get(SelectPin) != 2:
    #     delay_time(0.000001)
    while True:
        if GPIO.input(SelectPin) == 0:
            break
    while True:
        if GPIO.input(SelectPin) == 1:
            break
    while True:
        if GPIO.input(SelectPin) == 0:
            break

# Read data from dht11
def data_get(SelectPin, Data):
    for i in range(40):
        while True:
            if GPIO.input(SelectPin) == 1:
                break
        cnt = 0
        while GPIO.input(SelectPin) == 1:
            cnt += 1
            if cnt > 10:
                print("Over Time")
                break
        if cnt > 5:
            Data[i] = 1
        else:
            Data[i] = 0

    # Pulse_cnt = 0
    # level = GPIO.input(SelectPin)

    # # Detect LOW
    # while level == 0:
    #     Pulse_cnt += 5
    #     delay_time(0.000005)
    #     level = GPIO.input(SelectPin)

    # # Detect HIGH
    # while level == 1:
    #     Pulse_cnt += 5
    #     delay_time(0.000005)
    #     level = GPIO.input(SelectPin)

    # # Error : ±10%
    # if 70 < Pulse_cnt < 90:
    #     # Data : 0
    #     return 0
    # elif 105 < Pulse_cnt < 135:
    #     # Data : 1
    #     return 1
    # elif 140 < Pulse_cnt < 180:
    #     # Data : Ready
    #     return 2
    # else:
    #     # Error
    #     return 3

# Detect an error
def checksum(Data):
    return 0

# Binary to decimal conversion
def convert(SourceData, GenerateData):
    for i in range(5):
        if i%2 == 0:
            GenerateData[i] = int(''.join(map(str, SourceData[i*8:(i+1)*8])), 2)
        else:
            tmp = SourceData[i*8:(i+1)*8]
            sum = 0
            for j in range(8):
                if tmp[j] == 1:
                    sum += 1/(2 ** (j+1))
            GenerateData[i] = sum

# Stops program for requested time (depends on system time)
def delay_time(DelayTime):
    StartTime = time.monotonic()
    ElapsedTime = 0
    while ElapsedTime < DelayTime:
        ElapsedTime = time.monotonic() - StartTime
