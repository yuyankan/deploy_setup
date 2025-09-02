#!/bin/bash

# 定义代理地址
# 将 "http://gateway.zscalertwo.net:10090" 替换为你的实际代理地址
# 如果你的代理需要用户名和密码，格式为 "http://username:password@proxy.address:port"
PROXY_ADDRESS="http://gateway.zscalertwo.net:10090"

# 构建 Docker 镜像并打上标签
# -t: 给镜像命名和版本号
# -f: 指定 Dockerfile 的路径
# .: 构建上下文，代表当前目录
#
# --build-arg: 将代理地址作为参数传递给 Dockerfile

echo "Starting Docker image build for model_notebook:202508..."

docker build \
  --build-arg http_proxy="${PROXY_ADDRESS}" \
  --build-arg https_proxy="${PROXY_ADDRESS}" \
  -t python_env_fastapi:202509 \
  -f Dockerfile \
  .

# 检查构建是否成功
if [ $? -eq 0 ]; then
  echo "✅ Docker image built successfully."
else
  echo "❌ Docker image build failed."
fi
