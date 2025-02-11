from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware
import requests
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # Allow your frontend development server
    "http://127.0.0.1:3000",  # Alternative address for localhost
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

class WeatherRequest(BaseModel):
    city: str

@app.post("/weather/")
async def get_weather(request: WeatherRequest):
    city = request.city
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found")

    data = response.json()
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
    }