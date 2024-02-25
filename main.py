import dht11_orglib

# Parameter
DATA_PIN = 17

# Variables
BitsData = [0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0]
DecimalData = [0, 0, 0, 0, 0]
Flag = 0
Humidity = 0
Temperature = 0

# main
while True:
    if Flag == 0:
        Flag = 1
        
        # Initialization
        dht11_orglib.init_dht11(DATA_PIN)

    # Get data
    # if dht11_orglib.data_get(DATA_PIN) == 2:
    for i in range(40):
        BitsData[i] = dht11_orglib.data_get(DATA_PIN)
    
    # Convert data(bit to decimal)
    dht11_orglib.convert(BitsData, DecimalData)
    
    # Check data
    if dht11_orglib.checksum(BitsData) == 0:
        # Correct data
        Humidity = 0
        Temperature = 0
        print("Humidity[%]:", Humidity, "Temperature[℃]:", Temperature)
    else:
        # Not correct data
        print("Error")
            
    # Reset Falg
    Flag = 0
