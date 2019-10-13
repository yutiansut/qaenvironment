# qaenvironment
quantaxis environment 


为了统一内部项目/ 多个docker等  出现的跨机器的局域网情况, 方便大家直接快速在多个项目中使用QA的setting设置, 提供 QAEnv


==========================================================================


## 使用

from qaenvironment import mongo_ip, mongo_uri, eventmq_ip, eventmq_port, eventmq_user, eventmq_password, eventmq_amqp



## 配置

### 数据库部分:


- MONGODB = mgdb(mgdb 是docker内部的容器识别号) / 192.168.x.x

- MONGODB_PORT 一般没人用


### 消息队列部分

- QAPUBSUB_IP=qaeventmq
- EventMQ_IP=qaeventmq
- QAPUBSUB_PORT=5672
- QAPUBSUB_USER=admin
- QAPUBSUB_PWD=admin
- QARUN_AMQP=pyamqp://admin:admin@qaeventmq:5672//


