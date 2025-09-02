# file usage:
## 1: mount:server pic 2 server-fastapi: 
    01_mount.sh
## 2: create image: 
    02_Dockerfile,
    requirement.txt,
    03_creat_image.sh(set proxy)
## 3: create container: 
    04_docker-cmopose.yml, 
    main.py,
    05_docker_con.sh: for quick start /end: bash docker_con.sh start/end

===================================================================================================================================


# 背景：外部访问server2的图片： url 格式
## 方案1： 在sever2上直接启动 web 服务
## 方案2： 在另外一个server上 启动代理-fastapi 访问 server2 图片； 外部应用url 即可：
## url -->server1: fastapi -->server2 图片

-----------------------------------------------------------------------------------------
## 以下为方案2的实施： 理论及部署(docker container)
## 1. container运行机理 也是整个解决方案的关键。

容器的隔离性： Docker 容器是一个与宿主机隔离的独立环境。容器内部无法直接访问宿主机的文件系统，更无法直接访问宿主机网络上的其他服务器。

卷挂载 (volumes)： 这是打破隔离，让容器访问外部文件系统的唯一方式。它遵循 宿主机路径:容器内路径 的规则。

宿主机路径：必须是运行 Docker 的那台服务器上的本地路径。

容器内路径：是你希望在容器内部访问该路径的位置。

端口映射 (ports)： 这是一个网络规则，它将宿主机上的一个端口映射到容器内部的端口，从而让外部请求能够访问容器内的服务。

#### 1. mount 命令 server2-->server1： 这是在 Linux 宿主机上，将 Windows 共享文件夹转换为本地路径的关键工具。它确保了 Docker 宿主机能够首先访问到文件。
#### 2. set compose volume: -->宿主机 server1-->container
'''container: docker-compose.yml
    volumes:
      # 将Docker宿主（Server A）上的本地路径挂载到容器内部
      # 左侧路径 /mnt/images 是Server1(fastapi server)上的，而不是147.121.160.30(图片server)上的
      - "/mnt/images:/data_mount"  
      - .:/app
'''

#### 3. container: 内部地址 程序访问
'''python file to run for fast api: main.py

IMAGE_SERVER_PATH = Path("/data_mount")
'''
整个流程可以概括为：
#### Server B (图片服务器) -> Server A (Docker 宿主) -> Docker 容器

-----------------------------------------------------------------------------------------
## 2. server2: mount server1：文件挂载/镜像

'''bash
sudo mount -t cifs //147.121.160.30/data /home/carenk/my_data/01_projects/04_isra/02_fastapi/mnt/images -o username=XXX,password=XXX,domain=AP,vers=3.0
# check error for mounting:
sudo dmesg | tail
'''
#### mount 的本质不是复制。它不会将数据从来源地全部复制到你的本地硬盘上。

mount 的真正作用：创建“通道”
mount 的作用更像是在你的文件系统中打开一扇门，让你能够通过这个门去访问另一个地方的内容。

你可以把你的 Linux 文件系统想象成一栋大楼。你正在访问的目录，比如 /home/carenk/my_data/...，就是大楼里的一间空房间。

当你执行 mount 命令时，你做的是：

在空房间上开一扇门：这个空房间就是你的挂载点（/mnt/images）。

将门连接到外部世界：这扇门连接到了另一个文件系统（//147.121.160.30/data），这个文件系统可能是另一个服务器上的硬盘，也可能是一个U盘或硬盘分区。

通过这扇门，你可以直接看到并操作另一个文件系统中的文件。当你对 /mnt/images 中的文件进行读写操作时，你的操作系统实际上是在远程服务器上进行这些操作，数据始终存储在原始位置。



### 1. server1(linux) 代理 图片server2（windows), 以便外部访问server2的图片： url 格式
