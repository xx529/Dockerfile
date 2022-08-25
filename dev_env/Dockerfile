FROM ubuntu:18.04

MAINTAINER Hang

#  apt 更新、系统工具
RUN apt update -y && \
    apt-get update && \
    apt -y upgrade && \
    apt-get upgrade && \
    apt-get install -y wget

# 设置时区
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# 设置中文字符集 否则与系统有中文交互时会报错
RUN apt install -y locales && locale-gen zh_CN.UTF-8
ENV LC_CTYPE zh_CN.UTF-8
ENV LANG zh_CN.UTF-8

# 常用工具
RUN apt install -y vim && \
    apt install -y git && \
    apt-get install -y build-essential && \
    apt-get install libsasl2-dev && \
    apt -y install python3-pip && \
    pip3 install -U pip -i https://pypi.doubanio.com/simple && \
    apt-get install unzip && \
    apt-get install libfreetype6-dev && \
    apt-get install pkg-config && \
    apt-get install libpng12-dev && \
    apt-get install pkg-config

# 安装ssh
RUN apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# 安装 miniconda 并升级
ENV PATH /opt/conda/bin:$PATH
RUN wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    sh Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm -rf Miniconda3-latest-Linux-x86_64.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    /bin/bash -c "source /root/.bashrc"
    
# 更改成 bash 
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# 升级 conda
RUN conda update -n base -c defaults conda

# 复制 Dockerfile
COPY . ./dockerfile/

# 安装 jupyterlab + extension
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --no-cache-dir -r ./dockerfile/jupyterlab.txt && \
    pip install 'jupyterlab>=3.0.0,<4.0.0a0' jupyterlab-lsp && \
    pip install 'python-lsp-server[all]'
    
    
# streamlit
RUN conda create -n py38-streamlit python=3.8 -y && \
    source activate py38-streamlit && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --use-deprecated=legacy-resolver --no-cache-dir -r ./dockerfile/py38-streamlit.txt && \
    pip install ipykernel && \
    python -m ipykernel install --user --name=py38-streamlit --display-name "py38-streamlit"
    
# python3.10
RUN conda create -n py310-base python=3.10 -y && \
    source activate py310-base && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --use-deprecated=legacy-resolver --no-cache-dir -r ./dockerfile/py310-base.txt && \
    pip install ipykernel && \
    python -m ipykernel install --user --name=py310-base --display-name "py310-base"

# development
RUN conda create -n py38-dev python=3.8 -y && \
    source activate py38-dev && \
    pip install --no-cache-dir torch torchvision torchaudio && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --use-deprecated=legacy-resolver --no-cache-dir -r ./dockerfile/py38-dev.txt && \
    pip install ipykernel && \
    python -m ipykernel install --user --name=py38-dev --display-name "py38-dev"

# c++
# RUN conda install -c conda-forge xeus-cling && \
#     conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/ && \
#     conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/ && \
#     conda install -c conda-forge -y xeus-cling && \
#     jupyter-kernelspec install --user /opt/conda/share/jupyter/kernels/xcpp11 && \
#     jupyter-kernelspec install --user /opt/conda/share/jupyter/kernels/xcpp14 && \
#     jupyter-kernelspec install --user /opt/conda/share/jupyter/kernels/xcpp17

# 启动 jupyterlab
CMD jupyter lab --ip 0.0.0.0 --no-browser --port=8888 --allow-root --NotebookApp.token=hang
