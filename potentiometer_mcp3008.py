"""
Script Name: potentiometer_mcp3008.py

Description:
This script uses the gpiozero library to read analog input from an MCP3008 ADC chip 
connected to a Raspberry Pi. Specifically, it reads input from a potentiometer connected 
to channel 0 of the MCP3008. The script displays the normalized value (between 0 and 1) 
and the corresponding voltage in the terminal. A delay is added to control the update frequency.

Features:
- Reads normalized analog values from MCP3008.
- Converts the value to a voltage based on the MCP3008's reference voltage.
- Displays the readings in a human-readable format.
- Includes graceful termination using KeyboardInterrupt.

Connections:
- MCP3008's SPI pins should be connected to the Raspberry Pi as follows:
  - CLK: GPIO 11
  - MOSI: GPIO 10
  - MISO: GPIO 9
  - CS: GPIO 8

Usage:
Run the script using Python. Ensure the MCP3008 and potentiometer are correctly wired, 
and SPI is enabled on the Raspberry Pi.

Note:
Ensure that the voltage changes match the value changes. 
If they do not match, verify that the SPI permission setup is correctly configured on your Raspberry Pi.

Example:
python3 potentiometer_mcp3008.py

Dependencies:
- gpiozero
- time
"""

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
