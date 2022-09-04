import socket

#建立TCP 客户端连接
TCP_Client_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定端口号(非必须)
TCP_Client_Socket.bind(('192.168.179.128',8080))
#与TCP服务端建立连接
TCP_Client_Socket.connect(('192.168.0.102',8080))
#发送信息
TCP_Client_Socket.send('OK'.encode())
#TCP接收信息
recv_data = TCP_Client_Socket.recv(1024)
print(recv_data.decode('GBK'))
#关闭连接
TCP_Client_Socket.close()