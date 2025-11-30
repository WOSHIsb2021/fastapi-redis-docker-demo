# FastAPI Redis Docker Demo

这是一个基于 Docker 的微服务架构演示项目。实现了 Web 服务、反向代理和缓存数据的持久化。

## 🛠 技术栈
- **Python / FastAPI**: 后端 API 服务
- **Docker & Docker Compose**: 容器化编排
- **Nginx**: 反向代理网关
- **Redis**: 缓存与计数器服务

## 🚀 如何运行
1. 克隆项目
   ```bash
   git clone https://github.com/WOSHIsb2021/fastapi-redis-docker-demo.git
   ```
2. 进入项目目录
   ```bash
    cd fastapi-redis-docker-demo
    ```
3. 启动服务
   ```bash  
    docker compose up -d
    ```
4. 访问测试

打开浏览器访问 http://localhost 查看计数器

访问 http://localhost/reset 重置计数

✨ 功能特性

[x] 基于 Nginx 的 80 端口转发

[x] Redis 数据持久化 (Volume 挂载)

[x] 独立的 Python 虚拟环境配置