from gpiozero import (
    MCP3008,
)  # Import the MCP3008 class from gpiozero for handling analog input.


def main():
    pot = MCP3008(channel=0)  # Create an MCP3008 object for the specified channel.

    while True:
        voltage = pot.value
        print(f"Voltage: {voltage:.2f} V")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exit program.")
