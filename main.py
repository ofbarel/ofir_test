# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import asyncio


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return  {"message": "Hello World"}



