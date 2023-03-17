from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def hello() -> JSONResponse:
    return JSONResponse({"Message": "Hello!"}, status_code=200)
