# example snippet from https://realpython.com/python-redis/ :)

import asyncio
import aioredis


async def main():
    redis = await aioredis.create_redis_pool('redis://0.0.0.0')
    await redis.set('my-key', 'value')
    value = await redis.get('my-key', encoding='utf-8')
    print(value)

    redis.close()
    await redis.wait_closed()

asyncio.run(main())