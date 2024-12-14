"""
Script Name: dim_led_with_potentiometer.py

Description:
This script uses the gpiozero library to control the brightness of an LED using a potentiometer. 
The potentiometer is connected to the MCP3008 ADC chip, which converts the analog signal to 
a digital value. The LED's brightness is adjusted via PWM based on the potentiometer's value.

Features:
- Reads analog input from a specified MCP3008 channel.
- Adjusts the LED brightness using PWM based on the potentiometer's input.
- Prevents flickering by turning off the LED when the potentiometer value is near zero.
- Accepts user-defined GPIO pin for the LED and MCP3008 channel for flexibility.

User Input:
- LED Pin: GPIO pin number where the LED is connected.
- MCP3008 Channel: Channel number (0-7) where the potentiometer is connected.

Usage:
1. Connect the MCP3008 to the Raspberry Pi following the proper SPI pin configuration.
2. Wire the potentiometer to one of the MCP3008's channels.
3. Connect an LED to the specified GPIO pin on the Raspberry Pi.
4. Run the script and enter the required pin numbers when prompted.

Example:
python3 dim_led_with_potentiometer.py

Dependencies:
- gpiozero
- time

Circuit Requirements:
- MCP3008 ADC chip connected to the Raspberry Pi's SPI interface.
- Potentiometer connected to one of the MCP3008's analog input channels.
- LED with a current-limiting resistor connected to a GPIO pin on the Raspberry Pi.

"""

from gpiozero import PWMLED, MCP3008
from time import sleep

led_pin = int(input("LED Pin: "))
mcp3008_channel = int(input("MCP3008 Channel: "))

led = PWMLED(led_pin)
potentiometer = MCP3008(channel=mcp3008_channel)

while True:
    sleep(0.1)
    print(f"Potentiometer Value: {potentiometer.value}")
    if potentiometer.value < 0.001:
        led.value = 0
        continue
    led.value = potentiometer.value
