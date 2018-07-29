FROM jboss/wildfly
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent
#RUN /opt/jboss/wildfly/bin/add-user.sh jolokia jolokia --silent
ADD ./deployments/hawtio-wildfly-2.0.2.war /opt/jboss/wildfly/standalone/deployments/
RUN /opt/jboss/wildfly/bin/add-user.sh -a -g admin hawtio hawtio --silent
ADD ./deployments/jolokia.war /opt/jboss/wildfly/standalone/deployments/
RUN /opt/jboss/wildfly/bin/add-user.sh -a -g jolokia jolokia jolokia --silent
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
