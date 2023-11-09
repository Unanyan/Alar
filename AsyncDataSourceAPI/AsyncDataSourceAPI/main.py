from fastapi import FastAPI
import aiosqlite
import asyncio
import json
import subprocess

app = FastAPI()

DATABASE_URL = "data.db"


async def get_data_from_db(db, query):
    # TODO move TimeoutError simulation to test
    # await asyncio.sleep(2)
    async with db.execute(query) as cursor:
        return await cursor.fetchall()


async def get_data_from_db_with_timeout(db, query, timeout=2):
    result = await asyncio.wait_for(get_data_from_db(db, query), timeout=timeout)
    return result


@app.get("/data")
async def get_data():
    async with aiosqlite.connect(DATABASE_URL) as db:
        query_1 = "SELECT * FROM data_1"
        query_2 = "SELECT * FROM data_2"
        query_3 = "SELECT * FROM data_3"

        tasks = [
            get_data_from_db_with_timeout(db, query_1),
            get_data_from_db_with_timeout(db, query_2),
            get_data_from_db_with_timeout(db, query_3),
        ]

        try:
            data_1, data_2, data_3 = await asyncio.gather(*tasks)

            # Convert the result into dictionaries
            formatted_data_1 = [{"id": row[0], "name": row[1]} for row in data_1]
            formatted_data_2 = [{"id": row[0], "name": row[1]} for row in data_2]
            formatted_data_3 = [{"id": row[0], "name": row[1]} for row in data_3]

            all_data = formatted_data_1 + formatted_data_2 + formatted_data_3
            all_data = sorted(all_data, key=lambda all_data: all_data["id"])

            return all_data
        except Exception as e:
            # TODO use logging module
            print(e)
            return []


if __name__ == "__main__":
    # Create tables, insert data into tables
    pre_script = "AsyncDataSourceAPI/AsyncDataSourceAPI/pre-script.py"
    subprocess.run(["python", pre_script])

    # run server
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
