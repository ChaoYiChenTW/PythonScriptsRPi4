from gpiozero import LED, Button
from signal import pause

BUTTON_PIN = 12
LED_PIN = 16

led = LED(LED_PIN)
button = Button(BUTTON_PIN)

def button_pressed():
    print("Button is pressed.")
    led.on()
    
def button_released():
    print("Button is released.")
    led.off()

button.when_pressed = button_pressed
button.when_released = button_released

pause()  # Keep the script alive.