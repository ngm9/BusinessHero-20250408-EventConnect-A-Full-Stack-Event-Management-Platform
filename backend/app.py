from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="EventConnect API", description="API for the EventConnect event management platform")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the EventConnect API"}

# TODO: Add routers for different resources (events, users, registrations, etc.)
# TODO: Implement authentication and authorization
# TODO: Set up database connection and models
# TODO: Implement AWS API Gateway integration