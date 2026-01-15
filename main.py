from fastapi import FastAPI
from models import main


app = FastAPI()



@app.post("/top-threats")
def top_threats(data):
    top_threats = main(data)
    return top_threats