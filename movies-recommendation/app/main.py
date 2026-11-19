from fastapi import FastAPI
import uvicorn
from app.rest import router as recommendations_router
from dotenv import load_dotenv

app = FastAPI(
    title="Recommendations",
    openapi_url="/recommendations/openapi.json",
    docs_url="/docs",
)

app.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

