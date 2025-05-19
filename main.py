from fastapi import FastAPI
from database.db import Base, engine
from routes.auth import registration, login
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
def hi():
	return {"hello from" : "pooz store"}


app.include_router(registration.router)
app.include_router(login.router)
