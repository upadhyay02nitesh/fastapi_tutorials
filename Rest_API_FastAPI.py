from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from datetime import datetime
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode='a'  # append to existing log file
)
logger = logging.getLogger(__name__)

class Tea(BaseModel):
    id: int
    name: str
    salary: float

tea_collection: List[Tea] = []

@app.get('/')
async def home():
    logger.info("Home endpoint called")
    return "Hello from FastAPI"

@app.get('/fun')
async def query_parameter(emp_id: str, name: str = "KAlua", id: int = None):
    logger.info(f"/fun GET called with emp_id={emp_id}, name={name}, id={id}")
    return f"Hello from FastAPI {id},{name} and {emp_id}"

@app.post('/fun')
async def add_tea(tea: Tea):
    logger.info(f"Add tea request received: {tea}")
    if tea:
        tea_collection.append(tea)
        logger.info(f"Tea added successfully: {tea}")
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": "Tea data added successfully",
                "added_record": tea.dict(),
                "timestamp": datetime.now().isoformat()
            }
        )
    else:
        logger.error("Add tea failed: no tea data received")
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "message": "Tea not found",
                "data": None,
                "timestamp": datetime.now().isoformat()
            }
        )

@app.get('/data')
async def get_tea():
    logger.info("Get tea request received")
    if tea_collection:
        tea_data = [tea.dict() for tea in tea_collection]
        logger.info(f"Returning tea data: {tea_data}")
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": "Tea data fetched successfully",
                "updated_record": tea_data,
                "timestamp": datetime.now().isoformat()
            }
        )
    else:
        logger.warning("No tea data found to return")
        return JSONResponse(
            status_code=404,
            content={
                "status": "error",
                "message": "No data found",
                "data": None,
                "timestamp": datetime.now().isoformat()
            }
        )

@app.put('/data/{updated_tea_id}')
async def update_tea(updated_tea_id: int, updated_tea: Tea):
    logger.info(f"Update tea request received for id={updated_tea_id} with data={updated_tea}")
    for index, tea in enumerate(tea_collection):
        if updated_tea_id == tea.id:
            tea_collection[index] = updated_tea
            logger.info(f"Tea updated successfully: {updated_tea}")
            return JSONResponse(
                status_code=200,
                content={
                    "status": "success",
                    "message": "Tea updated successfully",
                    "updated_record": updated_tea.dict(),
                    "timestamp": datetime.now().isoformat()
                }
            )
    logger.error(f"Tea update failed: id {updated_tea_id} not found")
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": "Tea not found",
            "data": None,
            "timestamp": datetime.now().isoformat()
        }
    )

@app.delete('/data/{delete_id}')
async def delete_tea(delete_id: int):
    logger.info(f"Delete tea request received for id={delete_id}")
    for index, tea in enumerate(tea_collection):
        if tea.id == delete_id:
            del_data = tea_collection.pop(index)
            logger.info(f"Tea deleted successfully: {del_data}")
            return JSONResponse(
                status_code=200,
                content={
                    "status": "Success",
                    "message": "Deleted successfully",
                    "deleted_data": del_data.dict(),
                    "timestamp": datetime.now().isoformat()
                }
            )
    logger.error(f"Tea delete failed: id {delete_id} not found")
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": "No deletion",
            "data": None,
            "timestamp": datetime.now().isoformat()
        }
    )
