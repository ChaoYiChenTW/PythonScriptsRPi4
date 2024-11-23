from gpiozero import LED, Button
from signal import pause

led_pin = int(input("LED Pin: "))
button_pin = int(input("Button Pin: "))\

led = LED(led_pin)
button = Button(button_pin)

button.when_pressed = led.on
button.when_released = led.off

pause()  # Keep the script alive.
