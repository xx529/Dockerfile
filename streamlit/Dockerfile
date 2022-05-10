FROM python:3.8.13-slim-bullseye

COPY ./* ./dockerfile/

# apt 更新
RUN apt update -y && apt-get update -y && apt -y upgrade

# 设置时区
RUN apt-get install -y tzdata && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
    
# 设置中文字符集 否则与系统有中文交互时会报错
RUN apt install -y locales && locale-gen zh_CN.UTF-8
ENV LC_CTYPE zh_CN.UTF-8
ENV LANG zh_CN.UTF-8

# 升级 pip
RUN pip3 install --upgrade setuptools && \
    python3 -m pip install --upgrade pip
    
# 安装 python 包
RUN pip3 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r /dockerfile/requirements.txt

CMD /bin/bash
