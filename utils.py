#拼接响应报文
def create_request_http(status,request_body):
    request_line = 'HTTP/1.1 %s\r\n'%status
    request_header = '\r\n'
    request_blank = '\r\n'
    request_data = request_line + request_header + request_blank + request_body

    return request_data