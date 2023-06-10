FROM ubuntu:20.04

MAINTAINER Hang

ENV DEBIAN_FRONTEND=noninteractive

# update
RUN apt update -y && \
    apt-get update && \
    apt -y upgrade && \
    apt-get upgrade && \
    apt-get install -y wget && \
    apt install -y vim && \
    apt install -y git && \
    apt-get install -y unzip && \
    apt-get install -y build-essential && \
    # time
    apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    # font
    apt install -y locales && \
    locale-gen zh_CN.UTF-8 && \
    # ssh
    apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

ENV LC_CTYPE zh_CN.UTF-8
ENV LANG zh_CN.UTF-8

# cuda
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb && \
    dpkg -i cuda-keyring_1.0-1_all.deb && \
    apt-get update && \
    apt-get -y install cuda && \
    rm -rf cuda-keyring_1.0-1_all.deb

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
COPY ./jupyterlab.txt /dockerbuild/jupyterlab.txt
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --no-cache-dir -r /dockerbuild/jupyterlab.txt && \
    pip install 'jupyterlab>=3.0.0,<4.0.0a0' jupyterlab-lsp && \
    pip install 'python-lsp-server[all]'

# python env
COPY ./requirements.txt /dockerbuild/requirements.txt
RUN conda create -n py38-llm python=3.8 -y && \
    source activate py38-llm && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --use-deprecated=legacy-resolver --no-cache-dir -r /dockerbuild/requirements.txt && \
    python -m ipykernel install --user --name=py38-llm --display-name "py38-llm"

# ports
EXPOSE 8888
EXPOSE 22

# start
COPY ./start.sh /start.sh
CMD sh /start.sh
