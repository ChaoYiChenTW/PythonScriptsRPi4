import serial
import time


def init_serial():
    ser = serial.Serial(
        "/dev/ttyACM0", 9600, timeout=1
    )  # Build the serial object (Port, Baudrate, Timeout)
    time.sleep(3)  # wait for the Arduino to initialize
    ser.reset_input_buffer()  # flush the input buffer
    print("Serial is ready.")

    try:
        while True:
            if ser.in_waiting > 0:  # if there is data in the input buffer
                line = ser.readline().decode("utf-8").rstrip()
                print(line)
    except KeyboardInterrupt:
        print("Keyboard Interrupt.")
    finally:
        ser.close()  # close the serial connection


if __name__ == "__main__":
    init_serial()
