FROM centos:7

MAINTAINER Brandon

RUN yum -y install python
RUN ./build $(which python)

EXPOSE 8080

ENTRYPOINT ["./launch"]

