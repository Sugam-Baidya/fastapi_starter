from contextlib import asynccontextmanager
from fastapi import APIRouter, Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from app.core.config import Settings
from app.db.database import create_db_and_tables, get_session

origins = ["*"]

# Create tables on startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    create_db_and_tables()
    print("✅ Database connected & tables created")

    yield

    # Shutdown logic (optional)
    print("Application shutdown")


app = FastAPI(lifespan=lifespan)
router = APIRouter(prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@router.get("/")
def read_root():
    return {"message": "API v1 root"}


app.include_router(router)
