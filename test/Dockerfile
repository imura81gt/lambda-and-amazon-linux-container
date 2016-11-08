FROM 137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest

RUN mkdir /app

WORKDIR /app

RUN yum install python27 python27-pip python27-devel python27-libs gcc  -y

ADD . .
RUN yum install $(echo $(cat yum.list)) -y

CMD pip install --no-cache-dir -r /app/requirements.txt -t /app/vendor

