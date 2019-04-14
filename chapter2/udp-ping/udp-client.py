#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

__author__ = 'levent_j'

from socket import *
import time

serverName = 'localhost'  # 服务器地址，本例中使用一台远程主机
serverPort = 12000  # 服务器指定的端口
client_socket = socket(AF_INET, SOCK_DGRAM)  # 创建UDP套接字，使用IPv4协议
client_socket.settimeout(1)  # 设置套接字超时值1秒

for i in range(0, 10):
    sendTime = time.time()
    message = ('Ping %d %s' % (i + 1, sendTime)).encode()  # 生成数据报，编码为bytes以便发送
    try:
        address = (serverName, serverPort)
        client_socket.sendto(message, address=address)# 将信息发送到服务器
        modifiedMessage, serverAddress = client_socket.recvfrom(1024)  # 从服务器接收信息，同时也能得到服务器地址
        rtt = time.time() - sendTime  # 计算往返时间
        print('Sequence %d: Reply from %s    RTT = %.3fs' % (i + 1, serverName, rtt))  # 显示信息
    except Exception as e:
        print('Sequence %d: Request timed out' % (i + 1))

client_socket.close()  # 关闭套接字
