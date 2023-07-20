/etc/init.d/ssh start
nohup python3 -m http.server 8080 --directory /home/report >/dev/null 2>&1 &
/opt/bin/entry_point.sh
