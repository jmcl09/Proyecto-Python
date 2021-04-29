#!/bin/bash
FROM docker.elastic.co/logstash/logstash-oss:7.12.0

USER root

RUN yum install -y python3
RUN python3 -m pip install -U pip
RUN python3 -m pip install -U setuptools
RUN pip install python-binance
RUN mkdir /usr/share/logstash/python
