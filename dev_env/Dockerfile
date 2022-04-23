FROM ubuntu:18.04

MAINTAINER Hang

# 复制
COPY . ./dockerfile/

# 设置 apt 并更新
RUN apt update -y && \
    apt-get update -y && \
    apt -y upgrade && \
    apt-get install -y wget

# 设置时区
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# 设置中文字符集 否则与系统有中文交互时会报错
RUN apt install -y locales && locale-gen zh_CN.UTF-8
ENV LC_CTYPE zh_CN.UTF-8
ENV LANG zh_CN.UTF-8

# 安装相关
RUN apt install -y vim && \
    apt install -y git
    
# 安装 miniconda
ENV PATH /opt/conda/bin:$PATH
RUN wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    sh Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \
    rm -rf Miniconda3-latest-Linux-x86_64.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    /bin/bash -c "source /root/.bashrc" && \
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ && \
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ && \
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ && \
    conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

# 更改成 bash 
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# python3.8 + jupyterlab + labextension
RUN conda create -n py38 python=3.8 -y && \
    source activate py38 && \
    conda install --no-cache-dir --yes --file requirements.txt && \
    conda install jupyterlab && \
    apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt -y install nodejs && \
    jupyter serverextension enable --py jupyterlab --user && \
    conda install lckr-jupyterlab-variableinspector && \
    conda install --pre jupyter-lsp && \
    jupyter labextension install @krassowski/jupyterlab-lsp && \
    conda install python-language-server[python] && \
    conda install theme-darcula

# python3.10
RUN conda create -n py310 python=3.10 -y && \
    source activate py310
   

CMD ["/bin/bash"]
