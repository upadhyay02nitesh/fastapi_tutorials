from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.extension import Limiter
from fastapi.responses import PlainTextResponse

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return PlainTextResponse("Too many requests", status_code=429)

@app.get("/")
@limiter.limit("1/minute")
async def home(request: Request):
    print("Request received",request) # 1. Method (GET, POST, etc.)
    print("Method:", request.method)

    # 2. URL
    print("URL:", request.url)

    # 3. Headers
    print("Headers:")
    for key, value in request.headers.items():
        print(f"  {key}: {value}")

    # 4. Query Parameters
    print("Query Params:", dict(request.query_params))

    # 5. Cookies
    print("Cookies:", request.cookies)

    # 6. Client IP
    client_host = request.client.host
    print("Client IP:", client_host)

    # 7. Body (if needed, only in POST/PUT)
    # body = await request.body()
    # print("Body:", body.decode())

    return {"message": "Hello, world!"}
