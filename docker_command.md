# check docker
docker ps -a

docker image ls

# 2. create image 
docker build -t image_name:tag . (note: have to cd to Dockerfile folder, and have Dockerfile)

#3. create container:
docker build --name my_container docker_image: tag


or 
recommand to use compose file: xxx.yml
docker compse -f xxx.yml up -d(后台）


# 4. check docker container log
docker logs containerid


# download docker volume:
docker run --rm -v grafana_volume_data:/data -v /my_tmp:/backup alpine tar -czf /backup/grafana_volume_data.tar.gz -C /data .
use ubuntu:
docker run --rm -v grafana_volume_data:/data -v /my_tmp:/backup ubuntu tar -czf /backup/grafana_volume_data.tar.gz -C /data .

# Docker 数据卷迁移命令：参数与命令全解析

## 完整命令示例
```bash
docker run --rm \
  -v my_new_volume:/data \
  -v /tmp:/backup \
  tar -xzf /backup/my_volume.tar.gz -C /data


# Docker 数据卷迁移命令参数解析

## 一、`docker run --rm`
- **作用**：启动一个 Docker 容器，并在容器运行结束后自动删除该容器（`--rm` 是核心参数）。
- **优势**：避免容器运行后残留无用进程或文件，保持系统环境清洁，尤其适合临时任务（如数据迁移）。


## 二、`-v my_new_volume:/data`
- **参数类型**：数据卷（Volume）挂载参数。
- **解析**：
  - `my_new_volume`：在当前服务器上创建的新数据卷名称（若不存在则自动创建）。
  - `:/data`：将新数据卷挂载到容器内部的 `/data` 目录，即容器内 `/data` 的所有操作都会同步到宿主机的 `my_new_volume` 数据卷。
- **核心目的**：为迁移的数据提供持久化存储的目标位置。


## 三、`-v /tmp:/backup`
- **参数类型**：主机目录挂载参数。
- **解析**：
  - `/tmp`：宿主机上存放备份文件（如 `my_volume.tar.gz`）的本地目录。
  - `:/backup`：将宿主机的 `/tmp` 目录挂载到容器内部的 `/backup` 目录，使容器能够直接访问宿主机的备份文件。
- **作用**：建立宿主机与容器之间的文件通道，让容器可以读取备份数据。


## 四、`tar -xzf /backup/my_volume.tar.gz -C /data`
- **命令类型**：容器内执行的文件解压命令（`tar` 是 Linux 下的归档工具）。
- **参数解析**：
  - `-x`：表示执行提取（解压）操作，从压缩包中释放文件。
  - `-z`：指定处理 gzip 压缩格式的文件（对应 `.tar.gz` 后缀的压缩包）。
  - `-f /backup/my_volume.tar.gz`：指定要解压的文件路径（容器内路径，对应宿主机 `/tmp/my_volume.tar.gz`）。
  - `-C /data`：指定解压的目标目录为容器内的 `/data`（即已挂载的 `my_new_volume` 数据卷），确保数据被写入正确位置。


## 执行结果验证
命令执行成功后：
1. 宿主机将新增 `my_new_volume` 数据卷，包含备份文件中的所有数据。
2. 可通过 `docker volume ls` 命令查看数据卷是否存在，通过 `docker volume inspect my_new_volume` 查看数据卷详情。
