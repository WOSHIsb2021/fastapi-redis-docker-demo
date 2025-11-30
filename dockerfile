FROM python:3.13-slim
WORKDIR /app

# 先拷贝依赖文件（利用 Docker 缓存机制，加速构建）
COPY requirements.txt .

# 直接装在容器的全局里，没问题
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
