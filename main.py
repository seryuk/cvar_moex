from fastapi import FastAPI
from models.cvar import CvarRequest, CvarResult
app = FastAPI()
@app.post("/")
async def cvar_request(cvar: CvarRequest)->CvarResult:
    result = CvarResult(cvar = 3)
    return result

if __name__ == "__main__":
    import uvicorn
    config = uvicorn.Config("main:app", port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()


