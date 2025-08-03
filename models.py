from sqlmodel import SQLModel, Field, Column, JSON
from typing import List, Optional

class Teclado(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=False)
    modelo: str = Field(index=False)
    interface: str = Field(index=False)
    tipo: str = Field(index=False)
    sistemas_compativeis: List[str] = Field(sa_column=Column(JSON), index=False)
    layout: str = Field(index=False)
    descanso_de_pulso: bool = Field(index=False)

class Mouse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=False)
    modelo: str = Field(index=False)
    tipo: str = Field(index=False)
    interface: str = Field(index=False)
    peso: Optional[float] = Field(default=None, index=False)
    dpi_max: int = Field(index=False)
    sensor: str = Field(index=False)

class Monitor(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=False)
    modelo: str = Field(index=False)
    tamanho: str = Field(index=False)
    resolucao: str = Field(index=False)
    taxa_atualizacao: str = Field(index=False)
    tempo_resposta: str = Field(index=False)
    tipo_painel: str = Field(index=False)
    entradas: List[str] = Field(sa_column=Column(JSON), index=False)
    ajuste_altura: bool = Field(index=False)

class Placadevideo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=False)
    modelo: str = Field(index=False)
    fabricante: str = Field(index=False)
    interface: str = Field(index=False)
    resolucoes_suportadas: str = Field(index=False)
    saidas_video: List[str] = Field(sa_column=Column(JSON), index=False)
    suporte_tecnologias: List[str] = Field(sa_column=Column(JSON), index=False)
    consumo: int = Field(index=False)
    alimentacao_extra: Optional[str] = Field(default=None, index=False)

class Fonte(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=False)
    modelo: str = Field(index=False)
    fabricante: str = Field(index=False)
    potencia: int = Field(index=False)
    tipo: str = Field(index=False)
    modularidade: str = Field(index=False)
    conectores: List[str] = Field(sa_column=Column(JSON), index=False)
    voltagem: str = Field(index=False)
    protecoes: List[str] = Field(sa_column=Column(JSON), index=False)
    eficiencia: str = Field(index=False)

class Headset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=False)
    modelo: str = Field(index=False)
    fabricante: str = Field(index=False)
    tipo_conexao: str = Field(index=False)
    compatibilidade: List[str] = Field(sa_column=Column(JSON), index=False)
    microfone: str = Field(index=False)
    tipo: str = Field(index=False)
    controle_volume: str = Field(index=False)

class Placamae(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=False)
    modelo: str = Field(index=False)
    fabricante: str = Field(index=False)
    socket: str = Field(index=False)
    chipset: str = Field(index=False)
    formato: str = Field(index=False)
    suporte_memoria: str = Field(index=False)
    armazenamento: List[str] = Field(sa_column=Column(JSON), index=False)
    saidas_video: List[str] = Field(sa_column=Column(JSON), index=False)