FROM rabbitmq:management

ADD rabbitmq.config /etc/rabbitmq/
ADD definitions.json /etc/rabbitmq/

RUN rabbitmq-plugins enable --offline rabbitmq_shovel rabbitmq_shovel_management

