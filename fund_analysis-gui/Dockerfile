FROM python:3.8.13-slim-bullseye

MAINTAINER Hang

# apt 更新
RUN apt-get update -y &&  \
    apt -y upgrade && \
    apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \
    apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get install -y curl && \
    apt-get clean && \
    apt-get autoclean

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir PyQt5 pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip cache purge

COPY ./Dockerfile /dockerbuild/Dockerfile-prod

CMD /bin/bash
