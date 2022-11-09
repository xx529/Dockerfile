FROM python:3.8.13-slim-bullseye

MAINTAINER Hang

# apt 更新
RUN apt update -y && \
    apt-get update -y &&  \
    apt -y upgrade &&  \
    apt install -y vim && \
    apt-get install libgomp1 libicu-dev

# 安装ssh
RUN apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# 设置时区
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# 安装 python 包
COPY ./requirements.txt /dockerbuild/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir  -i https://pypi.tuna.tsinghua.edu.cn/simple -r /dockerbuild/requirements.txt

COPY ./Dockerfile /dockerbuild/Dockerfile

CMD /bin/bash