import socket

#建立TCP 客户端连接
TCP_Client_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定端口号
TCP_Client_Socket.bind(('192.168.179.128',8080))

#被动监听端口（最大允许128个链接）
TCP_Client_Socket.listen(128)

#接受TCP客户端连接，并产生新的 TCP 连接端口
New_TCP_Socket, IP_Adrr = TCP_Client_Socket.accept()

while True:
#TCP接收信息
    recv_data = New_TCP_Socket.recv(1024)
    print(recv_data.decode('GBK'))
    if not recv_data:
        print ('连接中断')
        break
    #TCP反馈信息
    New_TCP_Socket.send('收到'.encode('GBK'))

#关闭新TCP连接
New_TCP_Socket.close()

#关闭客户端连接
TCP_Client_Socket.close()