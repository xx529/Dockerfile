FROM ubuntu:18.04

# 设置 apt 并更新
RUN apt update -y && apt-get update -y && apt -y upgrade

# 设置时区
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# 设置中文字符集 否则与系统有中文交互时会报错
RUN apt install -y locales && locale-gen zh_CN.UTF-8
ENV LC_CTYPE zh_CN.UTF-8
ENV LANG zh_CN.UTF-8

# 安装相关
RUN apt install -y vim 
RUN apt install -y git

CMD /bin/bash
