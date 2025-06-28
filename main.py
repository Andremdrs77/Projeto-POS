from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from models import *

app = FastAPI()

teclados: List[Teclado] = []
mouses: List[Mouse] = []
monitores: List[Monitor] = []
placasdevideo: List[Placadevideo] = []
fontes: List[Fonte] = []
headsets: List[Headset] = []
placasmaes: List[Placamae] = []

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
