from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import json
import numpy as np

app = FastAPI()
model = SentenceTransformer("all-MiniLM-L6-v2")

# Carrega base de conhecimento
with open("banco_conhecimento.json", "r", encoding="utf-8") as f:
    conhecimento = json.load(f)

corpus = [item["contexto"] for item in conhecimento]
respostas_base = [item["resposta"] for item in conhecimento]

# Indexação vetorial
vetores = model.encode(corpus, convert_to_numpy=True)
index = faiss.IndexFlatL2(vetores.shape[1])
index.add(vetores)

# API
class Pergunta(BaseModel):
    texto: str

@app.post("/ia/compatibilidade")
def responder(pergunta: Pergunta):
    vetor = model.encode([pergunta.texto], convert_to_numpy=True)
    D, I = index.search(vetor, k=5)
    termos_pergunta = set(pergunta.texto.lower().split())

    resultados = []
    resposta_por_componente = {}

    for idx in I[0]:
        contexto = corpus[idx].lower()
        resposta = respostas_base[idx]

        if termos_pergunta.intersection(set(contexto.split())):
            resultados.append({"contexto": corpus[idx], "resposta": resposta})

            for termo in termos_pergunta:
                if termo in contexto:
                    if termo not in resposta_por_componente:
                        resposta_por_componente[termo] = set()
                    resposta_por_componente[termo].add(resposta)

    if not resultados:
        resposta_final = "Não foi possível encontrar informações específicas sobre os componentes mencionados. Verifique os nomes ou experimente componentes mais comuns."
    else:
        resumo = []
        for comp, respostas_set in resposta_por_componente.items():
            comp_respostas = list(respostas_set)
            incompat = [r for r in comp_respostas if "Incompatível" in r]
            compat = [r for r in comp_respostas if "Compatível" in r]

            if incompat:
                resumo.append(incompat[0])
            elif compat:
                resumo.append(compat[0])

        resposta_final = " ".join(sorted(set(resumo)))

    return {
        "pergunta": pergunta.texto,
        "resposta_final": resposta_final,
        "respostas_relevantes": resultados
    }