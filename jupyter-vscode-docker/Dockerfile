FROM ubuntu:20.04

MAINTAINER Hang

# 安装 docker 命令行工具和 docker compose
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release && \
    curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo \
    "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
    $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y docker-ce-cli && \
    curl -L https://get.daocloud.io/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# 设置 Docker 主机环境变量
ENV DOCKER_HOST unix:///var/run/docker.sock

# 不用手动输入时区
ENV DEBIAN_FRONTEND=noninteractive

# 安装相关工具
RUN apt install -y vim && \
    apt install -y git && \
    apt install -y curl && \
    apt-get install -y build-essential && \
    apt-get install libsasl2-dev && \
    apt -y install python3-pip && \
    pip3 install -U pip -i https://pypi.doubanio.com/simple && \
    apt-get install -y unzip && \
    apt-get install -y libfreetype6-dev && \
    apt-get install -y pkg-config && \
    apt-get install -y libpng-dev && \
    apt-get install -y libpq-dev && \
    apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

ENV LC_CTYPE zh_CN.UTF-8
ENV LANG zh_CN.UTF-8

# Miniconda
ENV PATH /opt/conda/bin:$PATH
RUN wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    sh Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm -rf Miniconda3-latest-Linux-x86_64.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    /bin/bash -c "source /root/.bashrc"

# default bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# update conda
RUN conda update -n base -c defaults conda

# jupyterlab + extension
COPY ./requirements/jupyterlab.txt /dockerbuild/requirements/jupyterlab.txt
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --no-cache-dir -r /dockerbuild/requirements/jupyterlab.txt

# python3.10
COPY ./requirements/py310.txt /dockerbuild/requirements/py310.txt
RUN conda create -n py310 python=3.10 -y && \
    source activate py310 && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --use-deprecated=legacy-resolver --no-cache-dir -r /dockerbuild/requirements/py310.txt && \
    pip install ipykernel && \
    python -m ipykernel install --user --name=py310 --display-name "py310"

# save resource
COPY ./Dockerfile /dockerbuild/
COPY ./resource /dockerbuild/resource

# code-server https://github.com/coder/code-server/releases
RUN wget  https://github.com/coder/code-server/releases/download/v4.16.1/code-server_4.16.1_amd64.deb --no-check-certificate
RUN dpkg -i code-server_4.16.1_amd64.deb && \
    mkdir /root/.config/code-server && \
    cp -f /dockerbuild/resource/code-server-config.yaml /root/.config/code-server/config.yaml && \
    rm -rf code-server_4.16.1_amd64.deb

# jupyterlab
EXPOSE 8888
# code-server
EXPOSE 8080
# ssh
EXPOSE 22

# start ssh, jupyterlab, code-server
CMD sh /dockerbuild/resource/start.sh
