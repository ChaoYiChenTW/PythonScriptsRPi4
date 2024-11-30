from gpiozero import (
    MCP3008,
)  # Import the MCP3008 class from gpiozero for handling analog input.
from time import sleep  # Import sleep to add a delay in the program.


def main():
    pot = MCP3008(
        channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8
    )  # Create an MCP3008 object for the potentiometer connected to channel 0.

    while True:
        value = pot.value
        voltage = pot.voltage
        print(f"Value: {value:.2f}, Voltage: {voltage:.2f} V")
        sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exit program.")
