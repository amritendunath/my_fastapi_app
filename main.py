from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()

@app.get("/")
async def health_check():
    return PlainTextResponse("Hello From Fastapi v4 and Successfully automated the backend workflow Yo")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload = True)