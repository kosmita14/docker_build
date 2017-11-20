FROM docker.elastic.co/logstash/logstash:6.0.0
RUN logstash-plugin install logstash-output-influxdb
RUN rm -f /usr/share/logstash/pipeline/logstash.conf
ADD pipeline/ /usr/share/logstash/pipeline/
ADD config/ /usr/share/logstash/config/
