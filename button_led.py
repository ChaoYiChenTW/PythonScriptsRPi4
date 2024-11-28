"""
GPIO Button-LED Control Script

This script demonstrates the use of the gpiozero library to control an LED using a push button
on a Raspberry Pi. The program allows users to specify the GPIO pins for the LED and button
and uses event-driven programming to turn the LED on when the button is pressed and off when
the button is released.

Key Features:
- Prompts the user to input GPIO pin numbers for the LED and button.
- Uses the gpiozero library's `LED` and `Button` classes for easy GPIO control.
- Event handlers (`when_pressed` and `when_released`) manage LED state changes.
- The script runs indefinitely, listening for button events, using the `pause()` function.

Prerequisites:
- Raspberry Pi with gpiozero installed.
- An LED connected to a GPIO pin with a current-limiting resistor.
- A push button connected to another GPIO pin.

How to Run:
1. Connect the LED and button to the Raspberry Pi's GPIO pins as per the hardware setup.
2. Run the script and provide the GPIO pin numbers when prompted.
3. Press and release the button to observe the LED behavior.

Author: Chao-Yi Chen
Date: 2024Nov27
"""

from gpiozero import (
    LED,
    Button,
)  # Import LED and Button classes from gpiozero for GPIO control.
from signal import pause  # Import pause to keep the script running and wait for events.

# Prompt the user to input the GPIO pin number connected to the LED.
led_pin = int(input("LED Pin: "))

# Prompt the user to input the GPIO pin number connected to the button.
button_pin = int(input("Button Pin: "))

# Create an LED object for the specified GPIO pin to control the LED.
led = LED(led_pin)

# Create a Button object for the specified GPIO pin to detect button presses.
button = Button(button_pin)

# Assign the LED's `on` method to the button's `when_pressed` event.
# This turns the LED on when the button is pressed.
button.when_pressed = led.on

# Assign the LED's `off` method to the button's `when_released` event.
# This turns the LED off when the button is released.
button.when_released = led.off

# Keep the script alive and listen for button press and release events.
pause()
