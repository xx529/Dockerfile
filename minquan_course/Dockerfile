FROM continuumio/anaconda3:2022.05

# 更新
RUN apt update -y && \
    apt-get update && \
    apt -y upgrade && \
    apt-get upgrade && \
    apt-get install -y wget

# 安装ssh
RUN apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
    
# 设置时区
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
    
# 更改成 bash 
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# 相关文件
COPY ./start.sh /dockerfile/
COPY ./Dockerfile /dockerfile/

# 端口
EXPOSE 8888
EXPOSE 22

# 启动
CMD sh /dockerfile/start.sh