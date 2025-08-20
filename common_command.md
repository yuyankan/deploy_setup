ip: xxx
id: carenk, password: xxx
change to : root:su -: password: Kun0987!shan

10.161.81.13:3000, grafana,id: admin, passwd: Avery@1234
#reset passwd: 
docker exec -it <your_container_id_or_name> grafana-cli admin reset-admin-password <new_password>
docker exec -it 6eec7dc9f5d6 grafana-cli admin reset-admin-password avery1234

10.161.81.13:8080, airflow,id: admin, passwd: admin

ssh: login:
ssh carenk@10.161.81.13
========================================
paste file::set paste
===============================================================================================
sever2:
ip :xxx
psw: xxx
ssh carenk@xxx
================================================================================================
TRANSFER FILE: sever1 to local/ server
scp -r carenk@10.161.81.13:/home/carenk /  C:\Users/0185972/myenv/ot_server/

scp -r C:\Users/0185972/myenv/ot_server/ carenk@10.161.67.41:/home/carenk/my_data/

==================
1. 停止所有正在运行的容器
docker stop $(docker ps -aq)

2. 删除所有容器
docker rm $(docker ps -aq)

3. 删除所有镜像

docker rmi $(docker images -q)
========================
transfer file:
scp "C:\Drivers\02_project\02_spc\01_etl_final\spc_etl_fun_v2.py" carenk@10.161.81.13:~/01_project/01_spc/02_etl/

scp "C:\Drivers\02_project\02_spc\01_etl_final\readme.txt" "C:\Drivers\02_project\02_spc\01_etl_final\spc_etl_main.py" "C:\Drivers\02_project\02_spc\01_etl_final\spc_etl_fun_v2.py" carenk@10.161.81.13:~/01_project/01_spc/02_etl/


scp "C:\Drivers\02_project\02_spc\01_etl_final\spc_etl_outlier_check_v2.py" "C:\Drivers\02_project\02_spc\01_etl_final\template_send_googlmail.py"  "C:\Drivers\02_project\02_spc\01_etl_final\template_send_googlchat.py"  "C:\Drivers\02_project\02_spc\01_etl_final\spc_etl_control_spec_calculate.py" carenk@10.161.81.13:~/01_project/01_spc/02_etl/

scp "grafana_volume_data_backup.tar" carenk@10.161.81.13:~/00_enviroment/02_container_airflow/

# 在你的本地电脑终端执行
scp "docker-compose.yaml" carenk@10.161.81.13:~/00_enviroment/02_container_airflow/

===================================================================================================
## check docker container setup:

sudo docker ps -a | grep Grafana-->查找container id
sudo docker inspect <grafana_container_id_or_name>-->查看container 设置
sudo docker inspect grafana | grep -A 5 -B 5 "PortBindings"--》查看Port

===============================================================================

#download image:
1. step: download
docker pull python:3.13-slim-bookworm
docker pull postgres:13
docker pull redis:7.2-bookworm
docker pull apache/airflow:2.9.3-python3.11

步骤 2: 将镜像保存为 .tar 文件
docker save -o python_3_13-slim_bookworm.tar python:3.13-slim-bookworm
docker save -o postgres_13.tar postgres:13
docker save -o redis_7_2_bookworm.tar redis:7.2-bookworm
docker save -o apache_airflow_2_9_3_python3_11.tar apache/airflow:2.9.3-python3.11

步骤 3: 通过 SSH 将 .tar 文件传输到服务器
scp python_3_13-slim_bookworm.tar carenk@10.161.81.13:~/00_enviroment/00_docker_images_tar
scp postgres_13.tar carenk@10.161.81.13:~/00_enviroment/00_docker_images_tar
scp redis_7_2_bookworm.tar carenk@10.161.81.13:~/00_enviroment/00_docker_images_tar
scp apache_airflow_2_9_3_python3_11.tar carenk@10.161.81.13:~/00_enviroment/00_docker_images_tar

步骤 4: 在服务器上加载镜像
# 在服务器上执行
cd /path/to/destination/ # 进入你传输文件到的目录
docker load -i python_3_13-slim_bookworm.tar
docker load -i postgres_13.tar
docker load -i redis_7_2_bookworm.tar
docker load -i apache_airflow_2_9_3_python3_11.tar
=====================================================
#查看 Docker 镜像存储的准确位置和驱动
docker info | grep -E "Storage Driver|Docker Root Dir"

================================================
#设置airflow 版本， 一遍在compose里引用：
# 打开 .env 文件
vim .env
在 .env 文件中添加或修改以下行：
AIRFLOW_IMAGE_NAME=apache/airflow:2.9.3-python3.11
=============================================================================================================

#set up python container
tar -xzvf python_.tar.gz

======================================================================================================
--Linux:python container

1.安装 pip download：
确保你的 pip 版本支持 download 命令。
pip freeze > requirements.txt

2.在你的 ~/my_etl_base_image 目录下，确保你有 requirements_base.txt 文件。

3.创建轮子文件存放目录：
创建一个新的目录来存放下载的 .whl 文件。例如，在 ~/my_etl_base_image 目录下：mkdir wheels

4.下载所有依赖到轮子目录：
pip download -r requirements.txt -d wheels/


# 使用pip download 下载所有依赖包到 wheels_linux 目录
# --platform linux_x86_64: 指定下载Linux x86-64架构的包
# --python-version 39: 指定Python 3.9版本（根据你的目标服务器Python版本调整）
# --only-binary :all: 强制下载预编译的wheel包，避免源码包
# --no-deps: 如果你的requirements.txt只包含顶层依赖，pip download会自动处理子依赖，但如果你想严格控制，可以不加此参数。
pip download -r requirements.txt --dest wheels_linux --platform linux_x86_64 --python-version 313 --only-binary :all:
pip download -r requirements.txt --dest wheels_linux --platform linux_x86_64 --python-version 312 --only-binary :all:


===================================================================================
步骤 2: 修改 Dockerfile
需要修改 Dockerfile，让 pip 在安装时从本地 wheels 目录查找包，而不是尝试连接互联网。
# my-org/etl-base/Dockerfile
FROM python:3.13-slim-bookworm

# 设置工作目录
WORKDIR /app

# 将 requirements_base.txt 和整个 wheels 目录复制到容器中
COPY requirements_base.txt .
COPY wheels/ wheels/ # 复制整个 wheels 目录

# 安装 Python 依赖
# --no-index: 告诉 pip 不要去 PyPI 索引查找包
# --find-links wheels/: 告诉 pip 从本地的 wheels/ 目录中查找包
RUN pip install --no-cache-dir --no-index --find-links wheels/ -r requirements_base.txt

# (可选) 设置默认的启动命令或入口点
# CMD ["python"]
===================================================================================================================================
步骤 3: 传输所有文件到离线服务器
现在，你需要将整个 ~/my_etl_base_image 目录下的所有内容（包括 Dockerfile、requirements_base.txt 和 wheels/ 目录）打包并传输到你的离线服务器。

打包成一个压缩文件 (可选，但推荐)：
cd ~/my_etl_base_image
tar -czvf etl_base_image_context.tar.gz .

通过 SCP 传输到服务器：
scp etl_base_image_context.tar.gz carenk@10.161.81.13:~/00_enviroment/01_python_common/wheels/

步骤 4: 在离线服务器上解压并构建镜像
# 在服务器上执行
cd /path/to/destination/
tar -xzvf etl_base_image_context.tar.gz


构建 Docker 镜像：
确保你位于解压后的目录中，然后执行构建命令：

=====================================================================================
基于提供的 Dockerfile、requirements.txt 和 wheel 文件夹来创建 ：
1. 构建 Docker 镜像：这是将你的 Dockerfile 和相关文件打包成一个可运行的镜像。
在你的终端中，确保你位于包含 Dockerfile、requirements.txt 和 wheel 文件夹的同一目录下。然后执行以下命令来构建镜像：
docker build -t python_common_env .

2. Building the Base Python Image
docker build -f Dockerfile.base -t common-python-etl:latest .

2.运行 Docker 容器：从你构建的镜像启动一个容器实例。

=====================================================================================
airflow container:
步骤 1: 获取 Docker Compose 文件
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'

步骤 2: 创建 .env 文件 (可选但推荐): vim .env
AIRFLOW_UID=$(id -u)
AIRFLOW_GID=$(id -g)

要在 Docker 中创建 Apache Airflow 容器，最推荐和最常用的方法是使用 Docker Compose。Airflow 官方提供了一个 docker-compose.yaml 文件，可以帮助你快速搭建一个包含所有必要组件的 Airflow 环境。

使用 Docker Compose 快速部署 Airflow
这个方法会启动 Airflow Webserver、Scheduler、Worker、PostgreSQL 数据库（用于元数据）和 Redis（用于 Celery Executor）。

步骤 1: 获取 Docker Compose 文件
首先，你需要下载 Apache Airflow 官方提供的 docker-compose.yaml 文件。

Bash

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.2/docker-compose.yaml'
(注意：请根据你希望使用的 Airflow 版本调整 URL 中的版本号，例如 2.9.2。你可以在 Airflow 官方文档 找到最新版本的链接。)

步骤 2: 创建 .env 文件 (可选但推荐)
在与 docker-compose.yaml 同级的目录下创建一个 .env 文件。这个文件可以用来定义一些环境变量，例如你的用户 ID 和组 ID，这有助于解决文件权限问题。

.env 文件内容示例：

Code snippet

AIRFLOW_UID=$(id -u)
AIRFLOW_GID=$(id -g)
这会将 Airflow 容器内运行的用户映射到你的宿主机用户，这样在宿主机和容器之间共享文件（如 DAGs）时就不会有权限问题。

3. 初始化 Airflow 数据库
docker compose up airflow-init

4. 启动 Airflow 服务
docker compose up -d
