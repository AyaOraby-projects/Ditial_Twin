from fastapi import FastAPI, File, UploadFile 
from pydantic import BaseModel 
from model import predict 
import uvicorn

app = FastAPI() 
@app.get("/")
async def home():
    return {"message": "Welcome to the Digital Twin API!"}


@app.post("/predict")
async def predict (input_image :UploadFile = File(...)):
    # Placeholder for file processing and prediction logic
    # In a real implementation, this would involve reading the file, processing it, and using the model to make predictions
    allowed_extensions = ["jpg", "jpeg", "png"]
    if input_image.filename.split(".")[-1].lower() not in allowed_extensions:
        return {"error": "Unsupported file type. Please upload a JPG or PNG image."}
    image_bytes = await input_image.read()
    prediction = predict( image_bytes)

    return ("prediction",prediction)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8001,reload=True)