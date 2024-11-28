from gpiozero import LED  # Import the LED class from the gpiozero library for controlling GPIO pins.
import time  # Import the time module for adding delays.

def main():
    """
    Main function to control an LED using GPIO.
    Prompts the user to input the GPIO pin connected to the LED,
    then toggles the LED on and off with a 1-second interval.
    """
    # Ask the user for the GPIO pin number where the LED is connected.
    led_pin = int(input("LED Pin: "))

    # Create an LED object for the specified GPIO pin.
    led = LED(led_pin)

    # Infinite loop to blink the LED.
    while True:
        led.on()  # Turn the LED on.
        time.sleep(1)  # Wait for 1 second.
        led.off()  # Turn the LED off.
        time.sleep(1)  # Wait for 1 second.

# Check if the script is run directly (not imported as a module).
if __name__ == "__main__":
    try:
        main()  # Call the main function.
    except KeyboardInterrupt:
        # Gracefully handle the program exit when Ctrl+C is pressed.
        print("Exit program.")
