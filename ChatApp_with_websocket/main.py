from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()

# 🔸 Dict to store connected clients: username -> WebSocket
connected_clients = {}


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    return FileResponse("static/index.html")

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    connected_clients[username] = websocket
    print(connected_clients)
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast to all connected users
            for client in connected_clients.values():
                await client.send_text(f"{username}: {data}")
    except WebSocketDisconnect:
        del connected_clients[username]
