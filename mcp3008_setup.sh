#!/bin/bash

ls -l /dev/spidev*

sudo usermod -aG spi $USER
sudo chmod 660 /dev/spidev*
sudo chown root:spi /dev/spidev*

ls -l /dev/spidev*