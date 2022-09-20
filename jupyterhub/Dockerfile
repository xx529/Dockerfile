FROM jupyterhub/jupyterhub:2

# system
RUN apt-get update && \
    apt install -y sudo vim wget git unzip && \
    apt-get install -y openssh-server openssh-client

# time
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Chinese font
RUN apt install -y locales && locale-gen zh_CN.UTF-8
ENV LC_CTYPE zh_CN.UTF-8
ENV LANG zh_CN.UTF-8

# jupyterlab and extensions
COPY ./config/jupyterlab.txt /dockerbuild/jupyterlab.txt
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    sudo -E pip install --no-cache-dir -r /dockerbuild/jupyterlab.txt && \
    sudo -E pip install 'jupyterlab>=3.0.0,<4.0.0a0' jupyterlab-lsp && \
    sudo -E pip install 'python-lsp-server[all]'

# default python env for users
COPY ./config/python38.txt /dockerbuild/python38.txt
RUN sudo -E pip install --no-cache-dir -r /dockerbuild/python38.txt

# read only folder shared to users
RUN sudo mkdir -p /srv/data/resource && \
    sudo ln -s /srv/data/resource /etc/skel/resource

# root
RUN echo root:root | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# admin
RUN useradd --no-log-init --shell /bin/bash admin && \
    adduser admin sudo && \
    echo "admin:admin" | chpasswd

# resource
RUN wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh
COPY ./config/SimHei.ttf /SimHei.ttf
COPY ./config/jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py
COPY ./config/adduser.py /adduser.py
COPY ./config/create_env.sh /create_env.sh
COPY ./config/start.sh /start.sh
COPY Dockerfile /dockerbuild/Dockerfile

# ports
EXPOSE 8000
EXPOSE 22

# start
CMD sh /start.sh