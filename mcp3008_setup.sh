#!/bin/bash
# Script Name: mcp3008_setup.sh

# Description:
# This script is used to configure SPI device permissions on a Raspberry Pi. 
# It ensures that the SPI devices (`/dev/spidev*`) are accessible by adding the current user to the SPI group, 
# updating file permissions, and changing the ownership of the SPI device files. 
# The script also lists the device permissions before and after the changes for verification.

# Steps Performed:
# 1. List the current permissions of SPI devices (`/dev/spidev*`).
# 2. Add the current user to the SPI group for access.
# 3. Update the permissions of SPI device files to allow read and write access for the SPI group.
# 4. Change ownership of the SPI devices to root and the SPI group.
# 5. List the updated permissions for verification.

# Usage:
# Run this script with appropriate privileges (e.g., as a user with `sudo` access).

# Example:
# sudo ./mcp3008_setup.sh

ls -l /dev/spidev*

sudo usermod -aG spi $USER
sudo chmod 660 /dev/spidev*
sudo chown root:spi /dev/spidev*

ls -l /dev/spidev*