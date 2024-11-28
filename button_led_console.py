"""
Push Button Control with Custom Functions

This script is designed as a learning exercise to demonstrate how to control
system behavior using a push button and custom functions. It uses the gpiozero
library to manage GPIO interactions on a Raspberry Pi. The script turns an LED
on when the button is pressed and off when the button is released, while
executing custom callback functions to print the button state.

Key Learning Objectives:
- Understanding how to use the gpiozero library for GPIO control.
- Implementing custom callback functions for button press and release events.
- Controlling hardware components (e.g., LEDs) based on button interactions.

Prerequisites:
- Raspberry Pi with gpiozero installed.
- An LED connected to the specified GPIO pin (with a resistor).
- A push button connected to the specified GPIO pin.

How to Use:
1. Connect the LED and button to the Raspberry Pi GPIO pins as specified in the script.
2. Run the script and observe the LED and console output when the button is pressed and released.

Author: Chao-Yi Chen
Date: 2024Nov27
"""

from gpiozero import LED, Button  # Import classes for GPIO control.
from signal import pause  # Import pause to keep the script running.

# Define the GPIO pins for the button and LED.
BUTTON_PIN = 12  # GPIO pin connected to the push button.
LED_PIN = 16  # GPIO pin connected to the LED.

# Initialize the LED and Button objects with the specified GPIO pins.
# Prompt the user to input the GPIO pin number connected to the LED.
led_pin = int(input("LED Pin: "))

# Prompt the user to input the GPIO pin number connected to the button.
button_pin = int(input("Button Pin: "))

# Create an LED object for the specified GPIO pin to control the LED.
led = LED(led_pin)

# Create a Button object for the specified GPIO pin to detect button presses.
button = Button(button_pin)


# Define a function to handle the button press event.
def button_pressed():
    """
    Custom function executed when the button is pressed.
    Turns the LED on and prints a message to indicate the button's state.
    """
    print("Button is pressed.")  # Display the current button state.
    led.on()  # Turn on the LED.


# Define a function to handle the button release event.
def button_released():
    """
    Custom function executed when the button is released.
    Turns the LED off and prints a message to indicate the button's state.
    """
    print("Button is released.")  # Display the current button state.
    led.off()  # Turn off the LED.


# Assign the custom functions to the button's press and release events.
button.when_pressed = (
    button_pressed  # Trigger `button_pressed` when the button is pressed.
)
button.when_released = (
    button_released  # Trigger `button_released` when the button is released.
)

# Keep the script running and listening for button events indefinitely.
pause()
