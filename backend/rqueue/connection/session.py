import redis


def get_redis_connection(host, port):
    return redis.Redis(
        host=host,
        port=port
    )
