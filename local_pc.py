import socket

from network_const import own_addr, arduino_addr


def run_socket(SHARED: dict):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(own_addr)
            while SHARED["thread_will_run"]:
                s.sendto(b"Hello, world", arduino_addr)
                
                data, addr = s.recvfrom(1024)
                print(f"Received {data!r}")
                if b"1" in data:
                    SHARED["current"] = 1
                else:
                    SHARED["current"] = 0
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Ending Process.")

