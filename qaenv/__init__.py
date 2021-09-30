import os


__author__ = 'yutiansut'
__version__ = '0.0.5'


mongo_ip = os.getenv('MONGODB', '127.0.0.1')
mongo_port =  os.getenv('MONGODBPORT', 27017)
mongo_uri = 'mongodb://{}:{}'.format(mongo_ip, mongo_port)


eventmq_ip = os.getenv('QAPUBSUB_IP', '127.0.0.1')
eventmq_port = os.getenv('QAPUBSUB_PORT', 5672)
eventmq_username = os.getenv('QAPUBSUB_USER', 'admin')
eventmq_password = os.getenv('QAPUBSUB_PWD', 'admin')
eventmq_amqp = 'pyamqp://{}:{}@{}:{}//'.format(
    eventmq_username, eventmq_password, eventmq_ip, eventmq_port)



clickhouse_ip =  os.getenv('CLICKHOUSE_IP', '127.0.0.1')
clickhouse_port =  os.getenv('CLICKHOUSE_PORT', 9000)
clickhouse_user =  os.getenv('CLICKHOUSE_USER', 'admin')
clickhouse_password =  os.getenv('CLICKHOUSE_PASSWORD', 'admin')

redis_ip = os.getenv('REDIS_IP', '127.0.0.1')
