from fastapi import FastAPI
import uvicorn


app = FastAPI(title="Pro Rider")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9500, reload=True, access_log=True)

    