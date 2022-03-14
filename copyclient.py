import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

s = socket.socket()
host = "10.0.0.118"
port = 5001
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected to ", host)
filecontents = input("Enter C for command or D for data file : ")
if filecontents == 'c': filename = "/Users/DanBallard/Desktop/commandfile.rtf"d
if filecontents == 'd': filename = "/Users/DanBallard/Desktop/bigfile.csv"
filesize = os.path.getsize(filename)
s.send(f"{filename}{SEPARATOR}{filesize}".encode())
#file = open(filename, 'wb')

progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as f:
    while True:
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            break
        s.sendall(bytes_read)
        progress.update(len(bytes_read))
s.close()