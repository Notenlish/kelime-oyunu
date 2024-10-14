from serial import Serial

ser = Serial("COM18")
while True:
    if ser.in_waiting > 0:
        inp = ser.read_all()
        decoded = inp.strip(b"\r").strip(b"\n")
        if b"1" in decoded:
            print("BASILDI")
        