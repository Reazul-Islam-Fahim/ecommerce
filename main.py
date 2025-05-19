from fastapi import FastAPI
from database.db import Base, engine
from routes.auth import registration, login

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def hi():
	return {"hello from" : "pooz store"}


app.include_router(registration.router)
app.include_router(login.router)
