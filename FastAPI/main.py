from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Hello FastAPI!"}

@app.post("/greet")
def greet_user(name: str):
    return {"message": "Hello, " + name + "!"}