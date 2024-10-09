from serial import Serial
import socket
import threading
import sys
import random
import time

global CURRENT
global THREAD_WILL_RUN
CURRENT: bool = False
THREAD_WILL_RUN = True


def run_serial(com: str):
    global CURRENT
    global THREAD_WILL_RUN
    ser = Serial(com, timeout=5)
    ser.open()
    try:
        while THREAD_WILL_RUN:
            if ser.in_waiting > 0:
                data = ser.readline().decode("utf-8").strip()

                if data == "0":
                    print("Received FALSE")
                    CURRENT = False
                elif data == "1":
                    print("Received TRUE!!!")
                    CURRENT = True
                else:
                    print(f"Unexpected data: {data}")
                    raise Exception("Unexpected data format.")
    except KeyboardInterrupt:
        print("KeyboardInterrupt. Ending Process.")
    finally:
        ser.close()


def run_serial_test(com: str):
    global CURRENT
    global THREAD_WILL_RUN
    while THREAD_WILL_RUN:
        print(THREAD_WILL_RUN)
        CURRENT = random.choice([False, True])
        time.sleep(0.05)


def main(HOST: str, PORT: int):
    global CURRENT
    global THREAD_WILL_RUN
    com = sys.argv[1]
    t = threading.Thread(target=run_serial_test, args=(com,))
    t.start()
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected to {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(str(int(CURRENT)).encode())
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Ending Process.")
        THREAD_WILL_RUN = False
        print("THREAD_WILL_RUN İS FALSE")
    finally:
        ...


if __name__ == "__main__":
    main("127.0.0.1", 12100)
