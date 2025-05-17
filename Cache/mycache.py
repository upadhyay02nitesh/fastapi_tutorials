# from fastapi import FastAPI
# import time
# from fastapi_cache import FastAPICache
# from fastapi_cache.coder import JsonCoder
# from fastapi_cache.backends.inmemory import InMemoryBackend
# from fastapi_cache.decorator import cache

# app = FastAPI()

# # ✅ Initialize cache at startup
# @app.on_event("startup")
# async def startup():
#     FastAPICache.init(InMemoryBackend(), coder=JsonCoder())

# # 🧪 Expensive route, takes 2 seconds
# @app.get("/slow-data")
# @cache(expire=10)  # Cache result for 10 seconds
# async def get_slow_data():
#     time.sleep(5)
#     return {"data": "This is slow, but cached!"}



from fastapi import FastAPI, HTTPException
import httpx
import time
from fastapi_cache import FastAPICache
from fastapi_cache.coder import JsonCoder
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache

app = FastAPI()

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), coder=JsonCoder())

@cache(expire=300)  # cache for 5 minutes
@app.get("/products/{product_id}")
async def get_product_detail(product_id: int):
    start_time = time.perf_counter()  # Start timer

    url = f"https://fakestoreapi.com/products/{product_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Product not found")
        product_data = response.json()

    end_time = time.perf_counter()  # End timer
    duration = end_time - start_time  # Calculate elapsed time in seconds

    return {
        "processing_time_seconds": round(duration, 4),  # e.g., 0.1234 seconds
        "product": product_data
    }
