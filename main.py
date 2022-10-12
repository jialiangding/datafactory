from fastapi import FastAPI

from app import fun










@fun.get("/")
async def root():
    return {"message": "Hello World"}

