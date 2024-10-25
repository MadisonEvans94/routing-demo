from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()


class QueryRequest(BaseModel):
    query: str


@app.post("/infer")
async def infer(request: QueryRequest):
    return {"response": request.query}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
