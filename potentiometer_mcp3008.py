from gpiozero import (
    MCP3008,
)  # Import the MCP3008 class from gpiozero for handling analog input.
from time import sleep  # Import sleep to add a delay in the program.


def main():
    channel = int(input("Channel: "))  # Ask the user for the MCP3008 channel number.

    pot = MCP3008(
        channel=channel,
        max_voltage=5.0,
    )  # Create an MCP3008 object for the specified channel.

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
