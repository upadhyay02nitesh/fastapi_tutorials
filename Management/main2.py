# from fastapi import FastAPI
# import time         # For synchronous sleep
# import asyncio      # For asynchronous sleep

# app = FastAPI()

# # Blocking tea server (sync)
# @app.get("/tea-blocking")
# def serve_tea_blocking():
#     time.sleep(5)  # Simulates making tea (blocking)
#     return {"message": "☕ Your tea is ready! (Blocking method)"}


# # Non-blocking tea server (async)
# @app.get("/tea-async")
# async def serve_tea_async():
#     await asyncio.sleep(2)  # Simulates making tea (non-blocking)
#     return {"message": "☕ Your tea is ready! (Async method)"}

# from fastapi import FastAPI, HTTPException
# import httpx  # Async HTTP client

# app = FastAPI()

# @app.get("/weather")
# async def get_weather(city: str = "London"):
#     try:
#         # Call public weather API (mock/demo API used)
#         async with httpx.AsyncClient() as client:
#             response = await client.get(f"https://wttr.in/{city}?format=3")  # simple weather output
#             if response.status_code != 200:
#                 raise HTTPException(status_code=500, detail="Failed to fetch weather")
#             return {"city": city, "weather": response.text}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


# ⚠️ This is Blocking:
# When one user hits /weather-blocking, the server:

# Sends a request to wttr.in

# Waits for the result (could take 2–10 seconds)

# During this time, the server worker is frozen

# Other users have to wait for this to finish

# 🚦 Real-World Problem
# Imagine you have only 1 or 2 workers (default for FastAPI):

# User A requests weather → waits 10 seconds

# User B requests anything else → must wait for A to finish!

# Your API feels slow, unresponsive

from fastapi import FastAPI, HTTPException
# import httpx
# import asyncio

# app = FastAPI()

# # Simulated microservices
# REVIEW_SERVICE_URL = "https://dummyjson.com/comments"
# STOCK_SERVICE_URL = "https://dummyjson.com/products/1"

# @app.get("/product/{product_id}")
# async def get_product_page(product_id: int):
#     try:
#         async with httpx.AsyncClient() as client:
#             # Fire all requests in parallel
#             product_url = f"https://dummyjson.com/products/{product_id}"
#             reviews_url = f"{REVIEW_SERVICE_URL}?postId={product_id}"
#             stock_url = f"{STOCK_SERVICE_URL}"

#             product_task = client.get(product_url)
#             review_task = client.get(reviews_url)
#             stock_task = client.get(stock_url)

#             product_res, review_res, stock_res = await asyncio.gather(
#                 product_task, review_task, stock_task
#             )

#             # Check if any request failed
#             if product_res.status_code != 200:
#                 raise HTTPException(status_code=404, detail="Product not found")

#             return {
#                 "product": product_res.json(),
#                 "reviews": review_res.json(),
#                 "stock": stock_res.json()
#             }

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

import time
from fastapi import FastAPI, BackgroundTasks
def write_log(message: str):
    with open("log.txt", "a") as log_file:
        time.sleep(5)
        log_file.write(f"{message}\n")
app = FastAPI()

@app.get("/notify/")
async def notify_user(name: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, f"Notified {name}")
    return {"message": f"Hi {name}, you will be notified soon!"}
# Background tasks are useful for:
# Sending emails    