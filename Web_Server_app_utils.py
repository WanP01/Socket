
#6.web_server服务器拆分模块化

import socket
import time

import app
import sys

class WebServer(object):
    def __init__(self,port):

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        server_socket.bind(('192.168.179.128', port))

        server_socket.listen(128)

        self.server_socket = server_socket

        print('已启动连接%s，端口号%s'%('192.168.179.128', port))

    def start(self):
        while True:
            new_socket, IP_addr = self.server_socket.accept()
            print('有新连接%s'%str(IP_addr))
            self.request_handler(new_socket,IP_addr)

            # new_socket, IP_addr = server_socket.accept()
            # request_handler(new_socket)
    def stop(self):
        self.server_socket.close()

    def request_handler(self,new_socket,IP_addr):

        recv_data = new_socket.recv(1024)
        print('已接受响应请求:\r\n%s'%recv_data.decode())

        if not recv_data:
            print ('客户服务器已断开')
            new_socket.close()
            return
        cur_path = 'web_test/templates'
        request_data = app.applications(recv_data,cur_path)

        new_socket.send(request_data.encode())

        new_socket.close()


def main():
    argv = sys.argv
    if len(argv) != 2:
        return print('你的输入参数有误，正确格式是\'python3 xxx.py portnum\'')
    if not argv[1].isdigit():
        return print('你输入的端口有误，正确格式是\'python3 xxx.py portnum\'')

    port = int(argv[1])

    Mini_WebServer = WebServer(port)
    # print(Mini_WebServer.new_socket)
    Mini_WebServer.start()
    Mini_WebServer.stop()

if __name__ == '__main__':
    main()


