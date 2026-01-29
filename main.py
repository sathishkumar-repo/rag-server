from fastapi import FastAPI, HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from routes import users

# Remove the broken SSL_CERT_FILE variable for this process
os.environ.pop("SSL_CERT_FILE", None)
os.environ.pop("REQUESTS_CA_BUNDLE", None) # Just in case this is also set

load_dotenv()

# Create FastAPI app 
app = FastAPI( 
	title = "Al Engineering",
	description="API for Six—figure Al Engineering application", 
	version="1.0.0"
)

# Configure CORS 
app.add_middleware(
	CORSMiddleware,
  allow_origins=["http://localhost:3000"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(users.router)

@app.get("/")
async def root():
  return {"message": "Welcome to the Al Engineering API!"}

@app.get("/health")
async def health_check():
  return {"status": "Healthy", "message": "The API is running smoothly."}

@app.get("/user/{user_id}")
async def get_user(user_id: int):
  return {"user_id": user_id, "name": f"User {user_id}", "role": "Engineer"}

  
if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) 
 