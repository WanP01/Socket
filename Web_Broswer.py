import socket
#web 浏览器为客户端（TCP）
#建立TCP连接
web_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接web 服务器
web_socket.connect(('192.168.179.128',8000))

#拼接Http协议
#请求行
http_line = 'GET /test/ HTTP/1.1 \r\n'
#请求头
http_header = 'HOST:192.168.179.128 \r\n'
#请求空行
http_blank = '\r\n'
#请求内容
#无
#拼接完整请求信息
request_data = http_line + http_header + http_blank
#发送请求信息
web_socket.send(request_data.encode())
#接收响应信息
recv_data = web_socket.recv(4096)

print(recv_data.decode())

web_socket.close()