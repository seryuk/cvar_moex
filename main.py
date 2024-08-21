from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"asdf": 543, "dsasd": 46465}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    import uvicorn

    config = uvicorn.Config("main:app", port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()
