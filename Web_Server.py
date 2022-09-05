import socket


class WebServer(object):
    def __init__(self):

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        server_socket.bind(('192.168.179.128', 8080))

        server_socket.listen(128)

        self.server_socket = server_socket

    def start(self):
        while True:
            self.new_socket, self.IP_addr = self.server_socket.accept()
            self.request_handler()
            # new_socket, IP_addr = server_socket.accept()
            # request_handler(new_socket)
    def stop(self):
        self.server_socket.close()

    def request_handler(self):

        recv_data = self.new_socket.recv(1024)
        print(recv_data.decode())

        if not recv_data:
            print ('客户服务器已断开')
            self.new_socket.close()
            return

        request_line = 'HTTP/1.1 200 OK\r\n'
        request_header = '\r\n'
        request_blank = '\r\n'
        #返回固定信息
        # request_body  = 'hello world'
        #返回固定页面
        # with open('web_test/templates/test1.html','r') as file:
        #     request_body = file.read()
        # print(type(request_body))
        #返回不同页面
        url = recv_data.decode().split()[1]
        if url == '/':
            url = '/index'
        try:
            with open('web_test/templates%s.html'%url,'r') as file:
                request_body = file.read()
            # with open('web_test/templates'+url+'.html','r') as file:
            #     request_body = file.read()
        except Exception as e:
            request_line = 'HTTP/1.1 404 Not Found\r\n'
            request_body = 'Error %s'%str(e)

        request_data = request_line + request_header + request_blank + request_body

        self.new_socket.send(request_data.encode())

        self.new_socket.close()



Mini_WebServer = WebServer()
# print(Mini_WebServer.new_socket)
Mini_WebServer.start()
Mini_WebServer.stop()


