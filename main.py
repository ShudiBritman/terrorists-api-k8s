from fastapi import FastAPI, UploadFile, File
from models import main


app = FastAPI()



@app.post("/top-threats/")
async def top_threats(data: UploadFile):
    top_threats = main(data)
    return top_threats




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)