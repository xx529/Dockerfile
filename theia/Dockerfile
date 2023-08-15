FROM hang529/theia:python

COPY . ./dockerfile

RUN apt update -y && \
    apt-get update -y && \
    apt -y upgrade && \
    apt-get upgrade && \
    apt-get install -y wget && \
    apt-get install -y build-essential && \
    apt-get install libsasl2-dev && \
    apt install -y vim && \
    apt install -y git

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

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
	pip install --use-deprecated=legacy-resolver --no-cache-dir -r ./dockerfile/requirement.txt
