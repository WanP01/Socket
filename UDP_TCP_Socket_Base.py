import socket

#创建套接字对象
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 绑定端口
addr = ('192.168.179.128',8888)
udp_socket.bind(addr)
# #套接字发送信息
# udp_socket.sendto('hello world'.encode(),('192.168.0.102',8080))
#广播发送(设置权限，默认禁止广播发送)
#socket.SOL_SOCKET 当前套接字
#socket.SO_BROADCAST 广播属性
#True 允许广播
udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,True)
#广播发送 192.168.179.255下的所有主机
udp_socket.sendto('hello world'.encode(),('192.168.0.255',8080))
#接收返回信息
recv_data = udp_socket.recvfrom(1024)#接收缓冲区大小
print(recv_data[0].decode(encoding = 'GBK',errors='ignore'),recv_data[1])
#关闭套接字
udp_socket.close()



tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_socket.close()