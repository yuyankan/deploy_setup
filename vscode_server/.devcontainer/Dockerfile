FROM python_env_common:202507

# 设置工作目录
WORKDIR /workspaces/my_project

# 复制你的依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制你的所有项目文件到容器中
COPY . .
