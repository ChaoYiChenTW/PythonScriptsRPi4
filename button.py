from gpiozero import Button
from signal import pause

def main():
    button_pin = int(input("Button Pin: "))
    button = Button(button_pin)

    button.when_pressed = button_pressed
    button.when_released = button_released

    pause()  # Keep the program alive.

def button_pressed():
    print("Pressed.")

def button_released():
    print("Released.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("exit program.")
