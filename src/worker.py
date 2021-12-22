
'''

worker file для обработки и очереди задач

'''

import redis
import os

os.chdir('../')

listen = ['default']

redis_url = 'redis://10.180.250.26:6379' #адрес не верный

conn = redis.from_url(redis_url)

with Connection(conn):
    worker = Worker(map(Queue,listen))
    worker.work()


