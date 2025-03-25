import asyncio
from aiohttp import web
import ssl

# 为不同域名准备证书和私钥
# 这里你需要替换为实际的证书和私钥文件路径
domain_certs = {
    'local.hipac.cn': {
        'cert': 'hipac.cn.pem',
        'key': 'hipac.cn.key'
    }
}

# 创建默认的 SSL 上下文
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# 可以设置一个默认的证书和私钥，用于处理未匹配到的域名
ssl_context.load_cert_chain(certfile='hipac.cn.pem', keyfile='hipac.cn.key')


async def handle(request):
    return web.Response(text="Hello, HTTPS World!")


async def main():
    app = web.Application()
    app.router.add_get('/', handle)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8443, ssl_context=ssl_context)
    await site.start()
    print("Server started at https://localhost:8443")
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
