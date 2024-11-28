from gpiozero import Button  # Import the Button class from gpiozero for handling GPIO input.
from signal import pause  # Import pause to keep the program running and wait for events.

def main():
    """
    Main function to test a push button using GPIO.
    Prompts the user for the GPIO pin connected to the button,
    then assigns functions to handle button press and release events.
    """
    # Ask the user for the GPIO pin number where the button is connected.
    button_pin = int(input("Button Pin: "))

    # Create a Button object for the specified GPIO pin.
    button = Button(button_pin)

    # Assign event handlers for button press and release actions.
    button.when_pressed = button_pressed  # Call button_pressed() when the button is pressed.
    button.when_released = button_released  # Call button_released() when the button is released.

    # Pause the program to wait for events indefinitely.
    pause()

def button_pressed():
    """Callback function to handle the button press event."""
    print("Pressed.")

def button_released():
    """Callback function to handle the button release event."""
    print("Released.")

# Check if the script is run directly (not imported as a module).
if __name__ == "__main__":
    try:
        main()  # Call the main function to start the program.
    except KeyboardInterrupt:
        # Gracefully handle program exit when Ctrl+C is pressed.
        print("Exit program.")
