import RPi.GPIO as GPIO
import time
import signal
import sys

def signal_handler(signal, frame):
    print("Program terminated")
    GPIO.cleanup()
    sys.exit(0)

def read_dht11(pin):
    data = []

    # ピンをLOWにしてセンサーに信号を送信
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.02)  # 20ms待機

    # ピンをHIGHにしてデータを読み取り開始
    GPIO.output(pin, GPIO.HIGH)
    GPIO.setup(pin, GPIO.IN)

    # ピンがLOWになるまで待機
    while GPIO.input(pin) == GPIO.LOW:
        continue

    # ピンがHIGHになるまで待機
    while GPIO.input(pin) == GPIO.HIGH:
        continue

    # データを読み取る
    for _ in range(40):
        while GPIO.input(pin) == GPIO.LOW:
            continue
        count = 0
        while GPIO.input(pin) == GPIO.HIGH:
            count += 1
            if count > 100:
                break
        data.append(count)

    # ピンを元に戻す
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

    return data

def parse_dht11_data(data):
    # データを解析して温度と湿度を取得
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    checksum_bit = data[32:40]

    humidity = int("".join([str(bit) for bit in humidity_bit]), 2)
    humidity_point = int("".join([str(bit) for bit in humidity_point_bit]), 2)
    temperature = int("".join([str(bit) for bit in temperature_bit]), 2)
    temperature_point = int("".join([str(bit) for bit in temperature_point_bit]), 2)
    checksum = int("".join([str(bit) for bit in checksum_bit]), 2)

    return humidity, temperature, checksum

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # プログラム終了時に割り込みハンドラを呼ぶ

    GPIO.setmode(GPIO.BCM)
    DHT_PIN = 4  # Raspberry PiのGPIOピン番号に合わせて設定

    while True:
        data = read_dht11(DHT_PIN)
        humidity, temperature, checksum = parse_dht11_data(data)

        if checksum == (humidity + temperature) % 256:
            print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
        else:
            print('Checksum error. Data may be invalid.')

        time.sleep(2)  # 適切なインターバルを設定