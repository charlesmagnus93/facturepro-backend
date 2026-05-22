from fastapi import FastAPI

app = FastAPI(title="FacturePro API")


@app.get("/")
def root():
    return {"message": "FacturePro API running"}
