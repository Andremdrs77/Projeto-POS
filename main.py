from fastapi import FastAPI
from pydantic import BaseModel
from ia.ia import responder_pergunta

app = FastAPI()

class Pergunta(BaseModel):
    texto: str

@app.post("/ia/compatibilidade")
def responder(pergunta: Pergunta):
    return responder_pergunta(pergunta.texto)
