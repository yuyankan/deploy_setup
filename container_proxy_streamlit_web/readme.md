# 1. container for streamlit web
# 2. nginx: proxy streamlit web: different from airflow, grafana, etc.

====================================
# compose file:
## common setup1 as velow
## others setup in .streamlt/config.toml 

version: '3.9'

services:
  streamlit:
    image: python_env_common_streamlit:202507
    container_name: streamlit_spc_maintain

    working_dir: /app/work
    volumes:
      - ./:/app/work
    networks:
      - shared_network
    expose:
      - "8501"  # 只在网络内部可见
    command: python -m streamlit run app_spc.py --server.port 8501 --server.address 0.0.0.0 --server.enableCORS false --server.enableXsrfProtection false

networks:
  shared_network:
    external: true
    name: network_docker_common_nginxuse
    # .streamlit/config.toml 与 docker-compose.yml 的区别与联系

.streamlit/config.toml 和 docker-compose.yml 是两个完全不同但又可能一起使用的配置文件，它们各自扮演着不同的角色。
=========================================================================================================================================================================
## .streamlit/config.toml
这是 Streamlit 应用的配置文件。它的作用是控制 Streamlit 应用的行为、样式和功能。这个文件位于你的 Streamlit 项目的根目录下的 .streamlit 文件夹中。

### 主要作用:
- 应用配置: 设置应用的标题、图标、主题等。
- 服务器配置: 控制 Streamlit 服务器的行为，例如端口号、是否启用 CORS、上传文件的大小限制等。
- 调试和性能: 调整缓存行为，显示或隐藏性能分析器。

### 举例:
```toml
# .streamlit/config.toml

[theme]
base="dark"
backgroundColor="#0A0B1A"
secondaryBackgroundColor="#111122"
textColor="#FFFFFF"

[server]
port = 8501
maxUploadSize = 200
```
=============================================================================================================================================================================
## docker-compose.yml

这是 Docker Compose 的配置文件。它的作用是定义和管理多个 Docker 容器应用。这个文件描述了你的整个应用栈（例如一个 Web 应用、一个数据库和一个消息队列）需要哪些服务，以及它们如何互相连接。

### 主要作用:
- 服务定义：定义每个容器服务（例如 webserver、database）使用的镜像、构建指令和环境变量。
- 网络和卷：定义容器之间的网络连接和数据持久化的卷。
- 运行参数：设置每个容器的端口映射、用户权限、资源限制等。

### 举例:
```yaml
# docker-compose.yml

version: '3.8'

services:
  streamlit-app:
    image: my-streamlit-image
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data

  database:
    image: postgres:14
    # 可补充数据库相关配置，如环境变量、卷挂载等
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
