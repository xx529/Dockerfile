FROM selenium/standalone-chrome-debug:latest

USER root

RUN apt-get update && \
    apt-get -y install python3-pip && \
    apt-get install -y default-jdk

RUN mkdir /opt/allure && \
    cd /opt/allure && \
    wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.15.0/allure-commandline-2.15.0.zip && \
    unzip allure-commandline-2.15.0.zip && \
    rm -f allure-commandline-2.15.0.zip && \
    ln -s /opt/allure/allure-2.15.0/bin/allure /usr/bin/allure

RUN apt-get install -y openssh-server openssh-client && \
    echo root:123456 | chpasswd && \
    echo "PermitRootLogin yes" >> /etc/ssh/sshd_config

RUN pip install --no-cache-dir requests -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir selenium pytest pytest-html allure-pytest pyautogui -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY ./Dockerfile /dockerbuild/Dockerfile
COPY ./start.sh /start.sh
RUN mkdir /home/report

EXPOSE 4444
EXPOSE 5900
EXPOSE 8080
EXPOSE 22

CMD sh /start.sh
