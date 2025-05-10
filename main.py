from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from api.whatsapp_routes import router as whatsapp_router

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="LipaChat API",
    description="WhatsApp AI Marketing & Customer Care Platform",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(whatsapp_router, prefix="/whatsapp", tags=["WhatsApp"])

@app.get("/")
async def root():
    return {"message": "Welcome to LipaChat API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 