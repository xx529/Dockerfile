/etc/init.d/ssh start
nohup code-server >/dev/null 2>log &
jupyter lab --ip 0.0.0.0 --no-browser --port=8888 --allow-root --NotebookApp.token=hang
