FROM golang:1.20.2

RUN apt update -y && \
    apt-get update -y &&  \
    apt -y upgrade && \
    apt install -y vim

# 安装ssh
RUN apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

# 设置 go
RUN go env -w GO111MODULE=on && \
    go env -w GOPROXY=https://goproxy.cn,direct

# 项目创建
WORKDIR /home/projcet
RUN mkdir src && \
    touch ./src/main.go && \
    go mod init project

 # 安装依赖
RUN go get "github.com/fsouza/go-dockerclient"

# 保存dockerfile
COPY ./Dockerfile /dockerbuild/Dockerfile
