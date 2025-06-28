from pydantic import BaseModel
from typing import List, Optional

class Teclado(BaseModel):
    interface: str  
    tipo: str  
    sistemas_compatíveis: List[str]  
    layout: str  
    descanso_de_pulso: bool  

class Mouse(BaseModel):
    tipo: str  
    interface: str  
    peso: Optional[float] = None  
    dpi_max: int  
    sensor: str  

class Monitor(BaseModel):
    tamanho: str  
    resolucao: str  
    taxa_atualizacao: str  
    tempo_resposta: str  
    tipo_painel: str  
    entradas: List[str]  
    ajuste_altura: bool  

class Placadevideo(BaseModel):
    modelo: str  
    fabricante: str  
    interface: str  
    resolucoes_suportadas: str  
    saidas_video: List[str]  
    suporte_tecnologias: List[str]  
    consumo: int  
    alimentacao_extra: Optional[str] = None  

class Fonte(BaseModel):
    modelo: str
    fabricante: str
    potencia: int  
    tipo: str  
    modularidade: str  
    conectores: List[str]  
    voltagem: str  
    protecoes: List[str]  
    eficiencia: str  

class Headset(BaseModel):
    modelo: str
    fabricante: str
    tipo_conexao: str  
    compatibilidade: List[str]  
    microfone: str  
    tipo: str  
    controle_volume: str  

class Placamae(BaseModel):
    modelo: str
    fabricante: str
    socket: str  
    chipset: str  
    formato: str  
    suporte_memoria: str  
    armazenamento: List[str]  
    saidas_video: List[str]  
