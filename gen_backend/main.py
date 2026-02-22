from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from gen_backend.routes import router

app = FastAPI()
app.include_router(router)
