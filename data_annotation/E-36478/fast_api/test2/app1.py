from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI()


# Define a route to the home page
@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Web App!"}


# Define another route
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


# Run the app using the uvicorn server
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)