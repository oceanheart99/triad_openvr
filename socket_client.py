import socket
HOST = '192.168.1.61'
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # cmd = raw_input("Please input msg:")
    # s.send(cmd)
    data = s.recv(1024)
    print data
