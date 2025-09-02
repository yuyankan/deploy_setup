#!/bin/bash

# 定义 Docker Compose 文件名
COMPOSE_FILE="docker-compose.yml"

# 定义容器名称以便于检查
CONTAINER_NAME="fastapi-app"

# 检查命令行参数
if [ "$1" == "start" ]; then
    echo "✅ Starting Docker container with $COMPOSE_FILE..."

    # 使用 docker compose up -d 启动容器
    docker compose -p llm -f "$COMPOSE_FILE" up -d

    # 检查容器是否成功启动
    if docker compose -p llm -f "$COMPOSE_FILE" ps | grep -q "$CONTAINER_NAME"; then
        echo "✅ Docker container '$CONTAINER_NAME' started successfully."
    else
        echo "❌ Failed to start Docker container."
        exit 1
    fi

elif [ "$1" == "end" ]; then
    echo "🛑 Stopping and removing Docker container defined in $COMPOSE_FILE..."

    # 使用 docker compose down 停止并移除容器
    docker compose -p llm -f "$COMPOSE_FILE" down

    # 检查容器是否已停止
    if ! docker compose -p llm -f "$COMPOSE_FILE" ps | grep -q "$CONTAINER_NAME"; then
        echo "✅ Docker container '$CONTAINER_NAME' stopped and removed successfully."
    else
        echo "❌ Failed to stop Docker container."
        exit 1
    fi
else
    echo "Usage: $0 start|end"
    echo "  start: Starts the Docker container."
    echo "  end: Stops and removes the Docker container."
    exit 1
fi
~      
