import socket

from network_const import own_addr, arduino_addr


def run_socket(SHARED: dict):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.bind(own_addr)
            thread_active = SHARED["thread_will_run"]
            while True:
                if thread_active:
                    print("asdas")
                    s.sendto(b"Hello, world", arduino_addr)
                    
                    data, addr = s.recvfrom(1024)
                    print(f"Received {data!r}")
                    if b"1" in data:
                        SHARED["current"] = 1
                    else:
                        SHARED["current"] = 0
                else:
                    # this daemon thread may actually memory leak, since while trying to get data if it cannot get it then it will just be in a blocking busy loop and it cant make it to the if not thread_active if statement
                    print("quitting the network socket thread")
                    break                
    except KeyboardInterrupt:
        print("Keyboard Interrupt. Ending Process.")
    print("quitted.")
    with open("L.txt","w") as f:
        f.write("L + ratio")

