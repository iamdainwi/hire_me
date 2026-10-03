from fastapi import FastAPI

from app.features.auth.router import router as auth_router

app = FastAPI(title="HireMe API")
app.include_router(auth_router, prefix="/api/v1")
