#FROM docker.elastic.co/logstash/logstash:5.6.3
FROM docker.elastic.co/logstash/logstash:6.0.0-rc2
RUN logstash-plugin install logstash-output-influxdb
#RUN logstash-plugin update logstash-output-elasticsearch
RUN rm -f /usr/share/logstash/pipeline/logstash.conf
ADD pipeline/ /usr/share/logstash/pipeline/
ADD config/ /usr/share/logstash/config/
