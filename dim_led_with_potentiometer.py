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
