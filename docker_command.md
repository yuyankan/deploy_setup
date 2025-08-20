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


# Docker 数据卷迁移命令：参数与命令全解析

## 完整命令示例
```bash
docker run --rm \
  -v my_new_volume:/data \
  -v /tmp:/backup \
  tar -xzf /backup/my_volume.tar.gz -C /data
