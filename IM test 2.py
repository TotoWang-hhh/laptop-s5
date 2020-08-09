import socket

#接受端的代码
client2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client2.bind(('127.0.0.1',4567))
while True:
    data,addr = client2.recvfrom(1024)
    print(addr,'--',data.decode('utf-8'))
    con = input()
    client2.sendto(con.encode('utf-8'),('127.0.0.1',8765))
