from fastapi import FastAPI


app = FastAPI()



@app.post("/top-threats")
def top_threats(data):
    pass