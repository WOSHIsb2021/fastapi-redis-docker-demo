# fastapi-redis-docker-demo

This is a simple demonstration of a FastAPI application that uses Redis as a database, all containerized using Docker.

## fastapi
使用FastAPI框架构建的Web应用程序，提供RESTful API接口。
## redis
使用Redis作为数据库，存储和检索数据。
## docker
使用Docker容器化应用程序，简化部署和管理。
### 快速开始
docker-compose up -d # 启动容器
docker-compose ps # 查看容器状态
docker-compose stop # 停止容器
docker-compose down # 删除容器
docker-compose logs -f # 查看日志