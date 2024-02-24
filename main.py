import dht11_orglib

# Parameter
DATA_PIN = 17

# Variables
DataBits = [0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0]
HIGH_Humidity = [0, 0, 0, 0, 0, 0, 0, 0]
LOW_Humidity = [0, 0, 0, 0, 0, 0, 0, 0]
HIGH_Temperature = [0, 0, 0, 0, 0, 0, 0, 0]
LOW_Temperature = [0, 0, 0, 0, 0, 0, 0, 0]
Parity_bit = [0, 0, 0, 0, 0, 0, 0, 0]
Humidity = 0
Temperature = 0
Parity = 0

# main
while True:
    dht11_orglib.init_dht11(DATA_PIN)
