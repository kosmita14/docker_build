FROM docker.elastic.co/elasticsearch/elasticsearch:6.0.1

RUN rm -f /usr/share/elasticsearch/config/elasticsearch.yml
RUN rm -f /usr/share/elasticsearch/config/log4j2.properties
RUN rm -f /usr/share/elasticsearch/plugins/ingest-geoip/jackson-annotations-2.8.2.jar
RUN rm -f /usr/share/elasticsearch/plugins/ingest-geoip/jackson-databind-2.8.2.jar

COPY elasticsearch.yml /usr/share/elasticsearch/config/
COPY log4j2.properties /usr/share/elasticsearch/config/
COPY java.policy $JAVA_HOME/lib/security/

RUN wget --output-document=/usr/share/elasticsearch/lib/jackson-databind-2.8.2.jar \
    http://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.8.2/jackson-databind-2.8.2.jar
RUN wget --output-document=/usr/share/elasticsearch/lib/jackson-annotations-2.8.2.jar \
    http://repo1.maven.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.8.2/jackson-annotations-2.8.2.jar

USER root

RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/config/elasticsearch.yml
RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/config/log4j2.properties
RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/lib/jackson-databind-2.8.2.jar
RUN chown elasticsearch:elasticsearch /usr/share/elasticsearch/lib/jackson-annotations-2.8.2.jar

USER elasticsearch
