from gpiozero import LED
import time

def main():
    led_pin = int(input("LED Pin: "))
    led = LED(led_pin)
    while True:
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exit program.")
