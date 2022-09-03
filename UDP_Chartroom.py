import socket

#函数主体
def main():
    #先创建链接Socket
    UDP_Socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定（监听）UDP端口
    UDP_Socket.bind(('192.168.179.128',8080))
    #绑定循环判断
    while True:
        print('1. 发送信息')
        print('2. 接收信息')
        print('3. 退出系统')

        sel_num = input('请输入你想要的功能序号\n')
        if sel_num == '1':
            send_msg(UDP_Socket)
        elif sel_num == '2':
            recv_msg(UDP_Socket)
        elif sel_num == '3':
            print('谢谢使用')
            print('系统已退出')
            break
        else:
            print('你输入的数字有误')

#发送函数
def send_msg(socket_exam):
    se_msg = input('你想要发送的信息\n')
    se_addr = input('你要发送的地址\n')
    se_port = input('你要发送的端口号\n')
    socket_exam.sendto(se_msg.encode(),(se_addr,int(se_port)))

#接收函数

def recv_msg(socket_exam):
    re_msg,re_addr = socket_exam.recvfrom(1024)
    print(re_msg.decode('GBK'),re_addr)

if __name__ == '__main__':
    main()