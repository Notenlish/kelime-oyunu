import threading
from serial import Serial
import socket
from socket import AF_INET, SOCK_DGRAM
from network_const import own_addr, arduino_addr

SHARED = {"out": 0, "thread_active": True}


def conn():
    with socket.socket(AF_INET, SOCK_DGRAM) as s:
        s.bind(arduino_addr)
        print(f"Connected to {own_addr}")
        while SHARED["thread_active"]:
            print("aAAAAAAA")
            # data, addr = s.recvfrom(1024)
            # if not data:
            #     print("NO DATA RECEIVED")
            out = str(SHARED["out"]).encode()
            print(out)
            s.sendto(out, own_addr)


try:

    t = threading.Thread(target=conn)
    t.start()

    ser = Serial("COM3")
    while True:
        if ser.in_waiting > 0:
            inp = ser.read_all()
            decoded = inp.strip(b"\r").strip(b"\n")
            if b"1" in decoded:
                SHARED["out"] = 1
            else:
                SHARED["out"] = 0
            out = str(SHARED["out"]).encode()
            # print(out)
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    pass
