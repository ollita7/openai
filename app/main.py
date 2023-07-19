from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health import routes as h_routes

app = FastAPI(title="Api", description="", root_path="")

app.include_router(h_routes.router, prefix="/health", tags=["Health check"])

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)