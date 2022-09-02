FROM python:3.8.13-slim-bullseye

COPY ./* ./dockerfile/

# apt 更新
RUN apt update -y && apt-get update -y && apt -y upgrade && apt install -y vim

# 安装ssh
RUN apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# 设置时区
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# 升级 pip
RUN pip3 install --upgrade setuptools && \
    python3 -m pip install --upgrade pip
    
# 安装 python 包
RUN pip3 install --no-cache-dir  -i https://pypi.tuna.tsinghua.edu.cn/simple -r /dockerfile/requirements.txt

CMD /bin/bash
