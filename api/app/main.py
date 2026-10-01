from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
def health():
    return JSONResponse(content="HirMe Server is runnig.....")