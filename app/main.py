from fastapi import FastAPI

app = FastAPI(title="Pro Rider")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port="9500", debug=True)

    