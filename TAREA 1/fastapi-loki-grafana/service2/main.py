from fastapi import FastAPI
import logging

app = FastAPI()

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Service 2: Root endpoint was called - Claudia Guzman - service2")
    return {"message": "Hello from Service 2!"}
