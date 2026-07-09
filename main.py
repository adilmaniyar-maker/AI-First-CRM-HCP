from app.api.routes.hcp import router as hcp_router
from fastapi import FastAPI
from app.api.routes.interaction import router as interaction_router
from app.database.database import Base, engine

# Import models so SQLAlchemy can discover them
from app.models.hcp import HCP
from app.models.interaction import Interaction

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI First CRM HCP",
    version="1.0.0"
)
app.include_router(hcp_router)
app.include_router(interaction_router)
@app.get("/")
def home():
    return {
        "message": "AI First CRM Backend Running Successfully"
    }