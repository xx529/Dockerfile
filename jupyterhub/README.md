# JupyterHub

## About

基于docker环境运行的jupyterhub服务，内置jupyterlab、相关实用的extension以及预安装好一个数据算法常用的python环境和依赖。根据以下说明可以快速配置新用户，同时为每个用户自动安装miniconda环境以及kernel。  

需要依赖：docker，docker-compose



## Run

克隆项目后，进入目录运行以下命令后会自动构建镜像以及自动运行jupterhub服务和ssh服务

```sh
docker-compose up
```



## Config

根据以下需要修改`docker-compose.yaml`文件

```yaml
ports: 
  - "8088:8000"  # jupterhub服务端口映射
  - "8022:22"    # 用户远程ssh登陆到容器内端口映射

volumes:
  - "~/your_data:/srv/data/resource"  # 挂载文件到此目录后，该目录下文件以只读形式共享给每个jupterhub用户
```



## Add user

容器内根目录提供一份`adduser.py`文件实现增加用户操作，免除需要在jupyterhub服务里新建用户后还需要在系统增加用户的操作，同时增加用户时候可以选择是否给用户自动安装miniconda环境。

1. 增加新用户，同时自动安装miniconda环境

   ```
   docker exec CONTAINER ID python3 /adduser.py -u username -p userpassword
   ```

2. 增加新用户，不提供miniconda环境

   ```
   docker exec CONTAINER ID python3 /adduser.py -u username -p userpassword --no_create_env
   ```

   

## Tips

*  **如果需要复用服务器已存在用户信息，登陆信息和密码信息等，也就是让容器内的用户与服务器一致则需要以下操作，此操作会让共享给每个用户的目录失效**

 1. `docker-compose.yaml`文件 `volumes`字段增加以下挂载信息

    ```yaml
    volumes:
      - "/etc/passwd:/etc/passwd"
      - "/etc/shadow:/etc/shadow"
      - "/etc/sudoers:/etc/sudoers"
      - "/home:/home"  # 用户主目录位置
    ```

 2. 在容器中执行命令为每个用户添加目录权限

    ```sh
    docker exec CONTAINER ID chown -R username /home/username
    ```

    

* **如果使用matplot出现中文字不显示，容器根目录提供了中文字体文件`SimHei.ttf`，根据相关命令配即可**