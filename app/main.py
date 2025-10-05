from fastapi import FastAPI
from .routes import auth_routes, product_routes

app = FastAPI(title="FastAPI E-Commerce API")

app.include_router(auth_routes.router)
app.include_router(product_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI E-commerce!"}
