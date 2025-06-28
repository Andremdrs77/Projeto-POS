from fastapi import FastAPI
from typing import List
from models import *
import json
from pathlib import Path

app = FastAPI()

# Caminho do arquivo de dados unificado
CAMINHO_JSON = Path(__file__).parent / "dados" / "componentes.json"

# Função para carregar os dados do JSON único e distribuir nas listas
def carregar_componentes():
    if not CAMINHO_JSON.exists():
        return {
            "teclados": [],
            "mouses": [],
            "monitores": [],
            "placasdevideo": [],
            "fontes": [],
            "headsets": [],
            "placasmaes": []
        }

    with open(CAMINHO_JSON, encoding="utf-8") as f:
        dados = json.load(f)

    return {
        "teclados": [Teclado(**item) for item in dados.get("teclado", [])],
        "mouses": [Mouse(**item) for item in dados.get("mouse", [])],
        "monitores": [Monitor(**item) for item in dados.get("monitor", [])],
        "placasdevideo": [Placadevideo(**item) for item in dados.get("placadevideo", [])],
        "fontes": [Fonte(**item) for item in dados.get("fonte", [])],
        "headsets": [Headset(**item) for item in dados.get("headset", [])],
        "placasmaes": [Placamae(**item) for item in dados.get("placamae", [])],
    }

# Inicializa listas a partir do arquivo JSON
componentes = carregar_componentes()

teclados = componentes["teclados"]
mouses = componentes["mouses"]
monitores = componentes["monitores"]
placasdevideo = componentes["placasdevideo"]
fontes = componentes["fontes"]
headsets = componentes["headsets"]
placasmaes = componentes["placasmaes"]

# GET ----------
@app.get("/componentes/teclados", response_model=List[Teclado])
def listar_teclados():
    return teclados

@app.get("/componentes/mouses", response_model=List[Mouse])
def listar_mouses():
    return mouses

@app.get("/componentes/monitores", response_model=List[Monitor])
def listar_monitores():
    return monitores

@app.get("/componentes/placas_de_video", response_model=List[Placadevideo])
def listar_placas_de_video():
    return placasdevideo

@app.get("/componentes/fontes", response_model=List[Fonte])
def listar_fontes():
    return fontes

@app.get("/componentes/headsets", response_model=List[Headset])
def listar_headsets():
    return headsets

@app.get("/componentes/placas_maes", response_model=List[Placamae])
def listar_placas_maes():
    return placasmaes

# POST ----------

@app.post("/componentes/teclados", response_model=Teclado)
def adicionar_teclado(teclado: Teclado):
    teclados.append(teclado)
    return teclado

@app.post("/componentes/mouses", response_model=Mouse)
def adicionar_mouse(mouse: Mouse):
    mouses.append(mouse)
    return mouse

@app.post("/componentes/monitores", response_model=Monitor)
def adicionar_monitor(monitor: Monitor):
    monitores.append(monitor)
    return monitor

@app.post("/componentes/placas_de_video", response_model=Placadevideo)
def adicionar_placadevideo(placadevideo: Placadevideo):
    placasdevideo.append(placadevideo)
    return placadevideo

@app.post("/componentes/fontes", response_model=Fonte)
def adicionar_fonte(fonte: Fonte):
    fontes.append(fonte)
    return fonte

@app.post("/componentes/headsets", response_model=Headset)
def adicionar_headset(headset: Headset):
    headsets.append(headset)
    return headset

@app.post("/componentes/placas_maes", response_model=Placamae)
def adicionar_placamae(placamae: Placamae):
    placasmaes.append(placamae)
    return placamae
