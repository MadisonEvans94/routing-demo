# main.py
import logging
from fastapi import FastAPI, HTTPException
from controller import Controller
from models import QueryRequest
from config import model_map
import httpx

app = FastAPI()

# Initialize the controller with model identifiers
controller = Controller(
    strong_model="mistral_7b_instruct", weak_model="llama_3_7b")


def post_query(query, endpoint):
    try:
        response = httpx.post(endpoint, json={"query": query})
        response.raise_for_status()
        return response.json()
    except httpx.HTTPStatusError as e:
        logging.error(f"Request to {endpoint} failed: {e.response.content}")
        raise HTTPException(status_code=e.response.status_code,
                            detail="Failed to get a response from the model service")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.post("/infer")
async def infer(request: QueryRequest):
    query = request.query
    model_id = controller.get_model(query)

    # Retrieve the model endpoint URL from the map
    url = model_map.get(model_id)
    if not url:
        logging.error(f"Model ID '{model_id}' not found in model map")
        raise HTTPException(status_code=404, detail="Model not found")

    logging.info(f"Model '{model_id}' selected with endpoint '{url}'")

    # Forward the query to the selected model's endpoint
    response = post_query(query, url)
    return {"response": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
