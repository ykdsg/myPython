import socket
import ssl

# 目标服务器的 IP 地址和端口
ip = '127.0.0.1'
port = 8443
# 目标服务器的域名
server_name = 'local.hipac.cn'

# 创建 SSL 上下文
ssl_context = ssl.create_default_context()

# 创建 TCP 套接字并连接到服务器
with socket.create_connection((ip, port)) as sock:
    # 设置超时时间（例如 10 秒）
    sock.settimeout(10)
    # 使用 SSL 包装套接字并传递 server_name
    with ssl_context.wrap_socket(sock, server_hostname=server_name) as ssock:
        # 发送 HTTP 请求
        request = b"GET / HTTP/1.1\r\nHost:127.0.0.1:8443\r\n\r\n"
        ssock.sendall(request)
        # 接收响应
        response = ssock.recv(4096)
        print(response.decode())
