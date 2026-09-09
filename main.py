from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# 1. Initialize the web server application
app = FastAPI()

# 2. Setup CORS (Cross-Origin Resource Sharing)
# This is crucial! It tells Python to allow your Vercel website to safely request data.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any web address (perfect for hackathons)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Define the structure of incoming data
class TravelRequest(BaseModel):
    city: str

# 4. Create the URL route that the frontend will call
@app.post("/get-tip")
def recommend_packing(request: TravelRequest):
    # This is your Python logic. We take the city input and make a decision tree.
    user_city = request.city.strip().lower()
    
    if user_city == "tokyo":
        tip = "Pack a Pasmo/Suica card app and light layers for navigating the metro network!"
    elif user_city == "london":
        tip = "Pack a compact umbrella and a windproof jacket. Rain is always a possibility!"
    elif user_city == "singapore":
        tip = "Pack breathable cotton clothing and high-SPF sunscreen for high humidity."
    else:
        tip = f"Pack your passport and universal adapters for your upcoming trip to {request.city}!"
        
    # Return a structured JSON package back to the internet
    return {"packing_tip": tip}
