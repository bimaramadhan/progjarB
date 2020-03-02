import socket
# import time

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(65), (TARGET_IP, TARGET_PORT))

# angka = 0

# while True:
#     angka = angka+1
#     msg = " ilham cok {} " . format(angka)
#     print(msg)
#     sock.sendto(msg.encode(), (TARGET_IP, TARGET_PORT))
#     time.sleep(1)

