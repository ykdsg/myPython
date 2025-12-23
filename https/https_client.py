import asyncio
import ssl

import aiohttp


# 这种方式没办法传递server_name ，除非关闭check hostname ，否则会报错
async def main():
    # 创建 SSL 上下文，用于验证服务器证书
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    # 加载服务器的证书文件，用于验证服务器身份
    # ssl_context.load_verify_locations('hipac.cn.pem')
    # 由于使用 IP 地址访问，需要手动设置服务器主机名
    # ssl_context.check_hostname = False

    headers = {
        'Host': 'local.hipac.cn'  # 手动设置 Host 头，模拟正常的域名访问
    }
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('https://127.0.0.1:8443', headers=headers, ssl=ssl_context) as response:
                print(await response.text())
        except aiohttp.ClientConnectorCertificateError as e:
            print(f"证书验证失败: {e}")
        except Exception as e:
            print(f"发生其他错误: {e}")


if __name__ == "__main__":
    asyncio.run(main())
