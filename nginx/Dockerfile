# Dockerfile
# 使用官方 Nginx 基础镜像
FROM nginx:latest

# 删除 Nginx 默认的配置，以便我们完全控制
RUN rm /etc/nginx/conf.d/default.conf

# 复制主 Nginx 配置文件到容器中
COPY nginx.conf /etc/nginx/nginx.conf

# 将所有独立的代理配置文件复制到 /etc/nginx/conf.d/ 目录
# 假设这些文件都在本地的 'conf.d' 目录中
COPY conf.d/ /etc/nginx/conf.d/

# 复制您的静态网页文件到 Nginx 服务的根目录
# 假设 Project1.html 和其他静态文件都在本地的 'html' 目录中
COPY html/ /usr/share/nginx/html/

# 暴露 Nginx 容器内部监听的端口 (在您的配置中是 80 端口)
EXPOSE 80

# Nginx 容器启动时默认运行的命令
CMD ["nginx", "-g", "daemon off;"]