# devcontainer.json、Dockerfile 和 docker-compose.yml 详解

本文将系统介绍 devcontainer.json、Dockerfile 和 docker-compose.yml 这三个文件的作用、核心功能、常用配置及相互关系，帮助你深入理解 Dev Containers 开发环境的工作机制。


## 1. devcontainer.json：VS Code 开发体验的指挥中心

devcontainer.json 是 Dev Container 技术栈的核心配置文件，主要作用是指导 VS Code 如何创建和配置开发环境。它本身不直接参与镜像构建或容器运行，而是通过引用其他文件（如 Dockerfile 或 docker-compose.yml）实现环境管理。

### 核心作用
- **定义开发环境类型**：指定使用单个 Docker 镜像还是多服务的 docker-compose.yml 配置。
- **配置 VS Code 行为**：包括自动安装扩展、设置工作区路径、配置端口转发等。
- **自动化环境初始化**：容器启动后自动执行命令（如安装项目依赖、配置工具）。

### 常见配置字段
- `"name"`：开发容器的名称（用于标识环境）。
- `"dockerComposeFile"`：指向 docker-compose.yml 文件的路径（多服务环境必填）。
- `"service"`：在多服务环境中，指定 VS Code 连接的目标服务名称。
- `"workspaceFolder"`：容器内的项目工作目录路径（如 `/workspace`）。
- `"extensions"`：启动后自动安装的 VS Code 扩展列表（格式为扩展 ID，如 `ms-python.python`）。
- `"postCreateCommand"`：容器创建后自动执行的命令（如 `pip install -r requirements.txt`）。
- `"forwardPorts"`：需要从容器映射到本地的端口列表（如 `8000`、`5432`）。
- `"features"`：预配置的工具集（如 `git`、`node`，可通过官方镜像快速添加）。

### 示例
```json
{
  "name": "Python Dev Environment",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "app",
  "workspaceFolder": "/app",
  "extensions": ["ms-python.python", "ms-azuretools.vscode-docker"],
  "postCreateCommand": "pip install -r requirements.txt",
  "forwardPorts": [8501],
  "features": {
    "ghcr.io/devcontainers/features/git:1": {}
  }
}
