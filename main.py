from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum
from pico_i2c_lcd import I2cLcd

# Constants for LCD
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

# Initialize I2C
i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)

# Initialize LCD
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# Clear the LCD screen
lcd.clear()

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

# Initialize the pin and DHT11 sensor
pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
    try:
        # Wait for 5 seconds
        time.sleep(5)
        
        # Measure temperature and humidity
        t_celsius = sensor.temperature
        t_fahrenheit = celsius_to_fahrenheit(t_celsius)
        h = sensor.humidity
        
        # Clear the LCD screen
        lcd.clear()
        
        # Display temperature and humidity on LCD
        lcd.putstr("Temp: {:.1f}F".format(t_fahrenheit))
        lcd.move_to(0, 1)
        lcd.putstr("Humidity: {:.1f}%".format(h))
    
    except InvalidChecksum:
        print("Invalid checksum received. Skipping measurement.")
    
    except Exception as e:
        print("An error occurred:", e)

