from fastapi import FastAPI, Request
from time import time,sleep
from typing import Dict

app = FastAPI()

# ✅ Fake DB for 10 users
fake_user_db: Dict[str, Dict[str, float]] = {
    f"user_{i}": {"visits": 0, "total_time": 0.0} for i in range(1, 11)
}

# ✅ Middleware to track time spent
@app.middleware("http")
async def track_time_middleware(request: Request, call_next):
    user_id = request.headers.get("user-id") or request.query_params.get("user_id")
    print(f"User ID: {user_id}")
    start = time()
    response = await call_next(request)
 
    duration_seconds = time() - start
    duration = round(duration_seconds / 60, 10)

    if user_id in fake_user_db:
        fake_user_db[user_id]["visits"] += 1
        fake_user_db[user_id]["total_time"] += duration
        print(f"[{user_id}] visited {request.url.path} in {duration}s")

    return response

# ✅ Sample endpoint
@app.get("/resource")
async def get_resource():
    sleep(10)
    return {"message": "This is a sample resource"}

# ✅ Check usage stats
@app.get("/usage/{user_id}")
async def get_usage(user_id: str):
    return fake_user_db.get(user_id, {"error": "User not found"})


