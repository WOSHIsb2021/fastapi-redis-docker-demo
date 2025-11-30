import os
from fastapi import FastAPI
import redis

app = FastAPI()

# 从环境变量里读取 Redis 的地址（这就是配置解耦！）
# 如果没读到，默认是 localhost（本地开发用），但在 Docker 里会读到 "my-redis"
redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.get("/")
def read_root():
    # 每次访问，让 Redis 里的 'hits' 键加 1
    # 如果键不存在，Redis 会自动创建并设为 1
    count = r.incr("hits")
    return {"Hello": "Dong", "Status": "Rising", "Visits": count}

@app.get("/reset")
def reset():
    flag = r.set("hits",0)
    return {"detail":"reseted","flag":flag}
