from fastapi import FastAPI
import asyncio

app = FastAPI()

async def fetch_data_source1():
    await asyncio.sleep(1)  # Simulate delay
    return {"source": "1", "data": "Data from source 1"}

async def fetch_data_source2():
    await asyncio.sleep(1)  # Simulate delay
    return {"source": "2", "data": "Data from source 2"}

@app.get("/fetch-data")
async def get_data():
    result1, result2 = await asyncio.gather(fetch_data_source1(), fetch_data_source2())
    return {"results": [result1, result2]}