#!/usr/bin/python
# -*- coding: utf-8 -*-

import aredis
import asyncio
import time


def my_handler(x):
    print(x)


async def use_pubsub_in_thread():
    client = aredis.StrictRedis()
    pubsub = client.pubsub()
    await pubsub.subscribe(**{'my-channel': my_handler})
    thread = pubsub.run_in_thread(daemon=True)
    for _ in range(10):
        await client.publish('my-channel', 'lalala')
    thread.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(use_pubsub_in_thread())
    asyncio.sleep(5)
