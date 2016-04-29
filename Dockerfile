FROM centos:7

MAINTAINER Brandon

RUN yum -y update
RUN yum -y install which python

RUN curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
RUN python get-pip.py
RUN pip install virtualenv

RUN mkdir -p /app/hello
COPY launch build /app/hello/
COPY src/ /app/hello/src/

WORKDIR /app/hello

RUN ls -l

RUN ./build

EXPOSE 8080

ENTRYPOINT ["./launch"]

