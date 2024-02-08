from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
import cv2
from classifier import (
    ImageClassifier,
)  # Make sure to import your ImageClassifier class correctly

app = FastAPI()

# Initialize your ImageClassifier here, assuming the ONNX model is in the same directory
classifier = ImageClassifier("mobilenet_v3_large.onnx")


@app.post("/classify-image/")
async def classify_image(file: UploadFile = File(...)):
    # Read the image file
    image_data = await file.read()
    nparr = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert BGR to RGB as your ImageClassifier expects RGB format
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Use the classifier to predict the image class
    predictions = classifier(img)

    # Return the predictions as a JSON response
    return JSONResponse(content={"predictions": predictions})
