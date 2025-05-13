from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from datetime import datetime
app=FastAPI()



class Tea(BaseModel):
    id:int
    name:str 
    salary:float

tea_collection:List[Tea]=[]


@app.get('/')
async def home():
    return "Hello from FastAPI"


@app.get('/fun')
async def query_parameter(id:int,emp_id:str):
    return f"Hello from FastAPI {id} and {emp_id}"

@app.post('/fun')
async def add_tea(tea:Tea):
    if tea:
        tea_collection.append(tea)
        return JSONResponse(status_code=200,
            content={
                "status":"success",
                "message": "Tea data added successfully",
                "added_record": tea.dict(),
                "timestamp":datetime.now().isoformat()
                }
            )
    return JSONResponse(status_code=200,
            content={
                "status":"error",
                "message": "Tea  not found",
                "data": None,
                "timestamp":datetime.now().isoformat()

            }
            )
    

@app.get('/data')
async def get_tea():
    if tea_collection:
        tea_data = [tea.dict() for tea in tea_collection]
        return JSONResponse(status_code=200,
                content={
                    "status":"success",
                    "message": "Tea updated successfully",
                    "updated_record": tea_data,
                    "timestamp":datetime.now().isoformat()
                    }
                )
    return JSONResponse(status_code=200,
            content={
                "status":"error",
                "message": "No data found",
                "data": None,
                "timestamp":datetime.now().isoformat()

            }
            )
    

@app.put('/data/{updated_tea_id}')
async def update_tea(updated_tea_id:int,updated_tea:Tea):
    for index,tea in enumerate(tea_collection):
        # print(index,tea)
        if updated_tea_id==tea.id:
            # print(updated_tea_id,tea.id)
            tea_collection[index]=updated_tea
            return JSONResponse(status_code=200,
            content={
                "status":"success",
                "message": "Tea updated successfully",
                "updated_record": updated_tea.dict(),
                "timestamp":datetime.now().isoformat()
                }
            )
    return JSONResponse(status_code=200,
            content={
                "status":"error",
                "message": "Tea  not found",
                "data": None,
                "timestamp":datetime.now().isoformat()
                }
            )

@app.delete('/data/{delete_id}')
async def delete_tea(delete_id:int):
    if delete_id:
        for index , tea in enumerate(tea_collection):
            if tea.id==delete_id:
                del_data=tea_collection.pop(index)
                return JSONResponse(
                    status_code=200,
                    content={
                        "status":"Success",
                        "message":"Deleted successfully",
                        "deleted_data":del_data.dict(),
                        "timestamp":datetime.now().isoformat()
                    }
                )
        return JSONResponse(status_code=200,
            content={
                "status":"error",
                "message": "No deletion",
                "data": None,
                "timestamp":datetime.now().isoformat()
                }
            )
