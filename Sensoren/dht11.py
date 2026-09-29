import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D24)

def read_dht():
        temp = sensor.temperature
        hum = sensor.humidity
        return temp, hum