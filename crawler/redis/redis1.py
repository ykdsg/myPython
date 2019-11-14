from redis import StrictRedis, ConnectionPool

redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', 'Bob')
print(redis.get('name'))
# 这样的连接效果是一样的。观察源码可以发现，StrictRedis 内其实就是用 host 和 port 等参数又构造了一个 ConnectionPool，所以直接将 ConnectionPool 当作参数传给 StrictRedis 也一样
pool = ConnectionPool(host='localhost', port=6379, db=0)
redis = StrictRedis(connection_pool=pool)
print(redis.get('name'))

# redis://[:password]@host:port/db 
url = 'redis://@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
print(redis.get('name'))
