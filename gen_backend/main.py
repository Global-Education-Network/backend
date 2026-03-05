from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gen_backend.routes import router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://global-education-network.onrender.com",
        "https://global-education-network.vercel.app",
        "http://localhost:8000",
        "http://localhost:5173",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
