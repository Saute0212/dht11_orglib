import RPi.GPIO as GPIO
import time

# GPIOピンの設定
GPIO_PIN = 17

# GPIOの初期化
GPIO.setmode(GPIO.BCM)
# GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 割り込み発生時のコールバック関数
def interrupt_callback(channel):
    if GPIO.input(channel):
        print("LOW->HIGH")
    else:
        print("HIGH->LOW")

def init_dht11(SelectPin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SelectPin, GPIO.OUT)
    GPIO.output(SelectPin, GPIO.HIGH)
    delay_time(0.5)
    GPIO.output(SelectPin, GPIO.LOW)
    delay_time(0.02)
    GPIO.output(SelectPin, GPIO.HIGH)
    GPIO.setup(SelectPin, GPIO.IN)

# Stops program for requested time (depends on system time)
def delay_time(DelayTime):
    StartTime = time.monotonic()
    ElapsedTime = 0
    while ElapsedTime < DelayTime:
        ElapsedTime = time.monotonic() - StartTime

# 割り込みイベントの設定
GPIO.add_event_detect(GPIO_PIN, GPIO.BOTH, callback=interrupt_callback)

print("waiting...")
while True:
    init_dht11(GPIO_PIN)
    delay_time(10)
