from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, create_engine, select
from models import Teclado, Mouse, Monitor, Placadevideo, Fonte, Headset, Placamae
from typing import Annotated
from contextlib import asynccontextmanager

# Configuração do banco
url = "sqlite:///banco.db"
engine = create_engine(url)

def get_session():
    with Session(engine) as session:
        yield session

def create_db():
    SQLModel.metadata.create_all(engine)

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

# -------- GET --------
@app.get("/componentes/teclados")
def listar_teclados(session: SessionDep) -> list[Teclado]:
    return session.exec(select(Teclado).limit(100)).all()

@app.get("/componentes/mouses")
def listar_mouses(session: SessionDep) -> list[Mouse]:
    return session.exec(select(Mouse).limit(100)).all()

@app.get("/componentes/monitores")
def listar_monitores(session: SessionDep) -> list[Monitor]:
    return session.exec(select(Monitor).limit(100)).all()

@app.get("/componentes/placas_de_video")
def listar_placas_video(session: SessionDep) -> list[Placadevideo]:
    return session.exec(select(Placadevideo).limit(100)).all()

@app.get("/componentes/fontes")
def listar_fontes(session: SessionDep) -> list[Fonte]:
    return session.exec(select(Fonte).limit(100)).all()

@app.get("/componentes/headsets")
def listar_headsets(session: SessionDep) -> list[Headset]:
    return session.exec(select(Headset).limit(100)).all()

@app.get("/componentes/placas_maes")
def listar_placas_maes(session: SessionDep) -> list[Placamae]:
    return session.exec(select(Placamae).limit(100)).all()

# -------- POST --------
@app.post("/componentes/teclados")
def adicionar_teclado(teclado: Teclado, session: SessionDep) -> Teclado:
    session.add(teclado)
    session.commit()
    session.refresh(teclado)
    return teclado

@app.post("/componentes/mouses")
def adicionar_mouse(mouse: Mouse, session: SessionDep) -> Mouse:
    session.add(mouse)
    session.commit()
    session.refresh(mouse)
    return mouse

@app.post("/componentes/monitores")
def adicionar_monitor(monitor: Monitor, session: SessionDep) -> Monitor:
    session.add(monitor)
    session.commit()
    session.refresh(monitor)
    return monitor

@app.post("/componentes/placas_de_video")
def adicionar_placa_video(placadevideo: Placadevideo, session: SessionDep) -> Placadevideo:
    session.add(placadevideo)
    session.commit()
    session.refresh(placadevideo)
    return placadevideo

@app.post("/componentes/fontes")
def adicionar_fonte(fonte: Fonte, session: SessionDep) -> Fonte:
    session.add(fonte)
    session.commit()
    session.refresh(fonte)
    return fonte

@app.post("/componentes/headsets")
def adicionar_headset(headset: Headset, session: SessionDep) -> Headset:
    session.add(headset)
    session.commit()
    session.refresh(headset)
    return headset

@app.post("/componentes/placas_maes")
def adicionar_placa_mae(placamae: Placamae, session: SessionDep) -> Placamae:
    session.add(placamae)
    session.commit()
    session.refresh(placamae)
    return placamae
