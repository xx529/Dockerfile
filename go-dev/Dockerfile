FROM golang:1.20.2

RUN apt update -y && \
    apt-get update -y &&  \
    apt -y upgrade

# 安装ssh
RUN apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config