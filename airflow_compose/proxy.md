# Airflow 反向代理配置：BASE_URL 与 ENABLE_PROXY_FIX 环境变量

`AIRFLOW__WEBSERVER__BASE_URL` 和 `AIRFLOW__WEBSERVER__ENABLE_PROXY_FIX` 这两个环境变量的作用是协同工作，以确保在**使用反向代理（如 Nginx）** 时，Airflow Webserver 能够正确生成所有链接。

## 一、AIRFLOW__WEBSERVER__BASE_URL

这个环境变量告诉 Airflow Webserver，外部用户访问它的完整 URL 是什么。

### 作用
Airflow 会使用这个 URL 来生成页面上的所有链接，例如：
- DAGs 列表中的每个 DAG 的链接。
- 任务实例日志的链接。
- Web UI 中的 API 终端链接。

### 示例
如果你的 Nginx 代理将所有指向 `http://your-domain.com/airflow-webserver` 的请求转发给 Airflow，那么 `BASE_URL` 环境变量就应该设置为 `http://your-domain.com/airflow-webserver`。

### 不正确配置的后果
如果你没有设置或者设置错误，Airflow 可能会生成类似 `http://airflow-webserver:8080/dags/my_dag_id` 的内部链接。当用户点击这些链接时，浏览器会无法解析，因为 `airflow-webserver` 这个域名只在 Docker 容器内部的网络中有效。

## 二、AIRFLOW__WEBSERVER__ENABLE_PROXY_FIX

这个环境变量的作用是让 Airflow 信任反向代理传递过来的请求头。

### 作用
当一个请求通过 Nginx 代理到达 Airflow 时，Nginx 会在请求头中添加一些信息，比如 `X-Forwarded-For`（用户的真实 IP 地址）和 `X-Forwarded-Proto`（原始请求协议，如 http 或 https）。

### 正确配置
将这个值设置为 `True`，Airflow 就会读取这些代理头，并根据它们来确定请求的真实来源和协议。这对于记录正确的客户端 IP 地址和确保 SSL/TLS 终止在代理层时，Airflow 仍能正确生成 https 链接至关重要。

### 不正确配置的后果
如果这个值设置为 `False`，Airflow 将会认为所有的请求都来自 Nginx（即 Docker 内部的 IP），并且可能会错误地生成 HTTP 链接，即使外部访问是通过 HTTPS 的。

## 总结

这两个环境变量是为了解决 “反向代理下 URL 不匹配” 的经典问题而设计的。

- `BASE_URL`：告诉 Airflow “你在外面的公开地址是什么”。
- `ENABLE_PROXY_FIX`：告诉 Airflow “从代理那里获取用户的真实信息”。

通过正确配置这两个变量，你可以确保通过 Nginx 代理访问的 Airflow Web UI 能够正常工作，并且所有链接和日志信息都是准确的。
