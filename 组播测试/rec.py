import sys
import struct
import time
import socket

mcast_group_ip = "239.255.255.252"
mcast_group_port = 23456
local_ip = "192.168.1.12"

def receiver():
    print(mcast_group_ip)
    print(local_ip)
    # 建立接收socket，和正常UDP数据包没区别
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.bind((local_ip, mcast_group_port))
    # 加入组播组
    mreq = struct.pack("=4sl", socket.inet_aton(mcast_group_ip), socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    # 允许端口复用
    # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 设置非阻塞
    # sock.setblocking(0)

    while True:
        try:
            message, addr = sock.recvfrom(1024)
            print(f'{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}: Receive data from {addr}: {message.decode()}')
        except :
            print("while receive message error occur")

if __name__ == "__main__":
    receiver()