1. container: 
for airflow only:
docker-compose.yml

2. container: add python container together:
docker-compose_python.yml

# 3. create folder manually: config,dags, logs, plugins
============================================================================================
# 3. airflow container: 与其他container 通信，使用：
## socket：

  # 通用卷挂载 (引用另一个锚点) - AIRFLOW_PROJ_DIR 的使用方式保持不变
  volumes: &airflow-common-volumes
    - airflow-dags:/opt/airflow/dags # 使用命名卷
    - airflow-logs:/opt/airflow/logs # 使用命名卷
    - airflow-config:/opt/airflow/config # 使用命名卷
    - airflow-plugins:/opt/airflow/plugins # 使用命名卷
    - /var/run/docker.sock:/var/run/docker.sock # <-- **Docker Socket 挂载已加入**

## network : set network_docker_common_nginxuse as docker network

networks: &airflow-common-network                                                                                                                                                                                 
 - airflow_network


networks:
  airflow_network:
    external: true
    name: network_docker_common_nginxuse
   

=========================================================================================
# airflow container: 用户权限管理：
'''
user: &airflow-common-user
  "${AIRFLOW_UID:-50000}:0"
group_add:
  # This GID must match the GID of the 'docker' group on your host.
  - 999
    '''
    # Docker Compose 中 group_add 指令的作用与原理

在 Docker Compose 中，`group_add` 指令允许你将容器内的用户添加到宿主机上指定的额外用户组中。这对于处理权限问题非常关键。

## 工作原理

1. **宿主机权限**：  
   在宿主机上，Docker 守护进程的 Unix 套接字（`/var/run/docker.sock`）的访问权限通常只允许 `root` 用户和 `docker` 用户组的成员访问。

2. **容器用户**：  
   你的 Airflow 容器以一个普通用户（例如，UID 1001 的 `airflow` 用户或 `default` 用户）运行。

3. **权限映射**：  
   当容器内的 `airflow` 用户尝试访问 `/var/run/docker.sock` 时，Linux 内核会根据它的 UID（1001）和 GID 来检查权限。

4. **group_add 的作用**：  
   `group_add: - 999` 这行配置告诉 Docker，在启动容器时，除了容器用户本身的用户组之外，还要将它添加到宿主机上 GID 为 999 的用户组中。

5. **解决问题**：  
   如果你已经确认了宿主机上 `docker` 用户组的 GID 正好是 999，那么通过这行配置，容器内的 `airflow` 用户就获得了访问 `/var/run/docker.sock` 所需的 `docker` 用户组权限，从而解决了 `Permission denied` 错误。

## 为什么不直接使用 user 指令？

你可能会问，为什么不直接在 `user` 指令中设置 GID？例如：`user: "${AIRFLOW_UID}:999"`。

- `user: <UID>:<GID>` 指令设置的是容器内的**主用户组**。
- `group_add` 指令则是在主用户组之外，**额外添加用户组**。

使用 `group_add` 的好处是，它不会改变容器内用户的默认主用户组，只是赋予了它额外的权限。这在很多情况下更灵活和安全，也更符合 Linux 的用户和用户组管理哲学。
