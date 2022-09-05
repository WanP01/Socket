import utils
def applications(recv_data,cur_path):
    # 返回固定信息
    # request_body  = 'hello world'
    # 返回固定页面
    # with open('web_test/templates/test1.html','r') as file:
    #     request_body = file.read()
    # print(type(request_body))
    # 返回不同页面
    url = recv_data.decode().split()[1]
    filepath = cur_path + '%s.html' % url

    if url == '/':
        url = '/index'
    try:
        with open(filepath, 'r') as file:
            request_body = file.read()
        # with open('web_test/templates'+url+'.html','r') as file:
        #     request_body = file.read()
            status = '200 OK'
    except Exception as e:
        request_body = 'Error %s' % str(e)
        status = '404 Not Found'

    print('已解析客户端想要访问的是%s,结果是%s'%(filepath,status))
    return utils.create_request_http(status,request_body)