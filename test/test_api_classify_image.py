import httpx
import pytest
from pathlib import Path


# Make sure the api in online.
@pytest.mark.asyncio
async def test_classify_image():
    # Assuming your FastAPI app is running on localhost:8000
    url = "http://localhost:8000/classify-image/"
    # Path to an image file you want to test with
    test_image_path = Path("test/data/bus.jpeg")

    # Open the image file in binary mode
    with test_image_path.open("rb") as f:
        # Create a dict containing the file to upload
        files = {"file": (test_image_path.name, f, "image/jpeg")}
        # Asynchronously send the request
        async with httpx.AsyncClient() as client:
            response = await client.post(url, files=files)
            # Ensure the request was successful
            assert response.status_code == 200
            # Optionally, you can also assert the structure of the response
            # For example, if your response is a JSON with a 'predictions' key
            response_data = response.json()
            assert "predictions" in response_data
