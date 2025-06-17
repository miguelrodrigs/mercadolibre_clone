from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("products.json") as f:
    products = json.load(f)

@app.get("/api/product/{product_id}")
async def get_product(product_id: str):
    product = products.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product