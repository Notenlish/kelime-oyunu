import threading

import socket


def run_socket(HOST: str, PORT: int, SHARED: dict):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while SHARED["thread_will_run"]:
                s.sendall(b"Hello, world")
                data = s.recv(1024)
                print(f"Received {data!r}")
                if data == b"0":
                    SHARED["current"] = 0
                elif data == b"1":
                    SHARED["current"] = 1
                else:
                    print("Got invalid data.")
                    raise Exception("Invalid Data.")
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Ending Process.")


if __name__ == "__main__":
    HOST = "127.0.0.1"  # The server's hostname or IP address
    PORT = 12100  # The port used by the server
    run_socket(HOST, PORT)
