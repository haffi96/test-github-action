from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/hello")
async def hello() -> JSONResponse:
    return JSONResponse({"Message": "Hello World!!"}, status_code=200)
