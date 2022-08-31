useradd --shell /bin/bash $NAME
adduser $NAME sudo
echo "$NAME:$PSW" | chpasswd
/etc/init.d/ssh start
jupyter lab --ip 0.0.0.0 --no-browser --port=8888 --allow-root --NotebookApp.token=$PSW