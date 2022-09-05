FROM ubuntu:20.04

MAINTAINER Hang

# update
RUN apt update -y && \
    apt-get update && \
    apt -y upgrade && \
    apt-get upgrade && \
    apt-get install -y wget

# time
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# font
RUN apt install -y locales && locale-gen zh_CN.UTF-8
ENV LC_CTYPE zh_CN.UTF-8
ENV LANG zh_CN.UTF-8

# useful tools
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
    apt-get install -y libpng-dev

# ssh user
RUN apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

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
    pip install --no-cache-dir -r /dockerbuild/requirements/jupyterlab.txt && \
    pip install 'jupyterlab>=3.0.0,<4.0.0a0' jupyterlab-lsp && \
    pip install 'python-lsp-server[all]'
    
# streamlit
COPY ./requirements/py38-streamlit.txt /dockerbuild/requirements/py38-streamlit.txt
RUN conda create -n py38-streamlit python=3.8 -y && \
    source activate py38-streamlit && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --use-deprecated=legacy-resolver --no-cache-dir -r /dockerbuild/requirements/py38-streamlit.txt && \
    pip install ipykernel && \
    python -m ipykernel install --user --name=py38-streamlit --display-name "py38-streamlit"
    
# python3.10
COPY ./requirements/py310-base.txt /dockerbuild/requirements/py310-base.txt
RUN conda create -n py310-base python=3.10 -y && \
    source activate py310-base && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --use-deprecated=legacy-resolver --no-cache-dir -r /dockerbuild/requirements/py310-base.txt && \
    pip install ipykernel && \
    python -m ipykernel install --user --name=py310-base --display-name "py310-base"

# development
COPY ./requirements/py38-dev.txt /dockerbuild/requirements/py38-dev.txt
RUN conda create -n py38-dev python=3.8 -y && \
    source activate py38-dev && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip install --no-cache-dir torch torchvision torchaudio && \
    wget https://data.pyg.org/whl/torch-1.12.0%2Bcpu/torch_cluster-1.6.0-cp38-cp38-linux_x86_64.whl && \
    pip install torch_cluster-1.6.0-cp38-cp38-linux_x86_64.whl && \
    rm -rf torch_cluster-1.6.0-cp38-cp38-linux_x86_64.whl && \
    wget https://data.pyg.org/whl/torch-1.12.0%2Bcpu/torch_scatter-2.0.9-cp38-cp38-linux_x86_64.whl && \
    pip install torch_scatter-2.0.9-cp38-cp38-linux_x86_64.whl && \
    rm -rf torch_scatter-2.0.9-cp38-cp38-linux_x86_64.whl && \
    wget https://data.pyg.org/whl/torch-1.12.0%2Bcpu/torch_sparse-0.6.14-cp38-cp38-linux_x86_64.whl && \
    pip install torch_sparse-0.6.14-cp38-cp38-linux_x86_64.whl && \
    rm -rf torch_sparse-0.6.14-cp38-cp38-linux_x86_64.whl && \
    wget https://data.pyg.org/whl/torch-1.12.0%2Bcpu/torch_spline_conv-1.2.1-cp38-cp38-linux_x86_64.whl && \
    pip install torch_spline_conv-1.2.1-cp38-cp38-linux_x86_64.whl && \
    rm -rf torch_spline_conv-1.2.1-cp38-cp38-linux_x86_64.whl && \
    pip install --use-deprecated=legacy-resolver --no-cache-dir -r /dockerbuild/requirements/py38-dev.txt && \
    pip install ipykernel && \
    python -m ipykernel install --user --name=py38-dev --display-name "py38-dev"

# save resource
COPY ./Dockerfile /dockerbuild/
COPY ./resource /dockerbuild/resource

# ports
EXPOSE 8888
EXPOSE 22

# start ssh and jupyterlab
CMD /etc/init.d/ssh start && jupyter lab --ip 0.0.0.0 --no-browser --port=8888 --allow-root --NotebookApp.token=hang
