import ssl

import requests

# 目标服务器的IP地址和端口
ip = '127.0.0.1'
port = 8443
# 目标服务器的域名
server_name = 'local.hipac.cn'

# 创建SSL上下文
context = ssl.create_default_context()
# 设置验证模式为CERT_REQUIRED，要求服务器提供证书并验证
context.verify_mode = ssl.CERT_REQUIRED
# 加载系统的证书颁发机构（CA）证书
context.load_default_certs()


# 创建自定义的HTTPAdapter
class SNIAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = requests.packages.urllib3.poolmanager.PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            block=block,
            ssl_context=context,
            assert_hostname=server_name
        )


# 创建会话
session = requests.Session()
# 为会话安装自定义的HTTPAdapter
session.mount(f'https://{ip}:{port}', SNIAdapter())

# 发送HTTP请求
url = f'https://{ip}:{port}'
response = session.get(url, headers={'Host': server_name})
print(response.text)
