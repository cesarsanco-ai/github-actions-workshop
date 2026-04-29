from fastapi import FastAPI

app = FastAPI(title="Ejemplo CI", version="0.1.0")


@app.get("/")
def hola_mundo():
    return {"message": "Hola Mundo"}
