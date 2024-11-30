import spidev

spi = spidev.SpiDev()
spi.open(0, 0)  # Open SPI bus 0, device 0
spi.max_speed_hz = 50000

response = spi.xfer2([0xAA])  # Send a test byte
print("SPI response:", response)

spi.close()
