# 以通用 Python ETL 镜像作为基础
FROM python_env_common_streamlit:202507

# 设置容器内的工作目录
WORKDIR /app/mywork

# 复制 project_A 的所有代码文件到容器中
COPY . .

# 暴露 Streamlit 默认端口
EXPOSE 8020

# 定义健康检查
# Streamlit 默认会在 /_stcore/health 端点提供健康检查
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8020/_stcore/health || exit 1

# 在容器启动时直接运行 Streamlit 应用程序
# 使用 'python -m streamlit' 更健壮，因为它直接通过 Python 解释器调用 Streamlit 模块
CMD ["python", "-m", "streamlit", "run", "app.py", "--server.port", "8020", "--server.address", "0.0.0.0"]