from fastapi import FastAPI

app = FastAPI(
    title="NutriVexa API",
    description="Backend API for personalized dietary management",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to NutriVexa API",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }