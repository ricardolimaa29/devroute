from pathlib import Path
from fastapi import FastAPI, HTTPException,Query
from fastapi.middleware.cors import CORSMiddleware
import json 

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "events.json"

app = FastAPI(
    title="DevRoute API",
    description=(
        "Agrega eventos de tecnologia do Brasil a partir de múltiplas fontes "
        "(feeds estruturados e scrapers best-effort) e retorna em JSON."
    ),
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def saude_da_API():
    return {
        "status": "ok",
        "version": "1.0.0"
}

def load_events():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


@app.get("/events",tags=["Events"])
def get_events(
    page: int = Query(default=1, ge=1, description="Número da página"),
    limit: int = Query(default=20, ge=1, le=20, description="Máximo de 20 itens por página")):
    dados = load_events()
    
    todos_eventos = dados.get("events", [])
    
    inicio = (page - 1) * limit
    fim = inicio + limit
    
    eventos_paginados = todos_eventos[inicio:fim]
    
    return eventos_paginados


# por ID
@app.get("/events/{id}",tags=["Events"])
def filtro_id(id: int):
    dados = load_events()
    # Buscando o evento pedido do 'ID'
    for evento in dados.get("events", []):
        if evento.get("id") == id:
            return evento
            
    # retorna o erro 404, caso nao encontre
    raise HTTPException(status_code=404, detail="Evento não encontrado")

# por cidade
@app.get("/events/city/{city}",tags=["Events"])
def filtro_city(city: str):
    dados = load_events()

    eventos_encontrados = []
    
    for evento in dados.get("events", []):
        
        if evento.get("city") and evento.get("city").lower() == city.lower():
            eventos_encontrados.append(evento)

    if not eventos_encontrados:
        raise HTTPException(status_code=404, detail="Nenhum evento encontrado para esta cidade")

    return eventos_encontrados

# por estado
@app.get("/events/state/{state}",tags=["Events"])
def filtro_state(state: str):
    dados = load_events()
    
    eventos_encontrados = []
    
    for evento in dados.get("events", []):
        
        if evento.get("state") and evento.get("state").lower() == state.lower():
            eventos_encontrados.append(evento)
            

    if not eventos_encontrados:
        raise HTTPException(status_code=404, detail="Nenhum evento encontrado para este estado")

    return eventos_encontrados

# por modalidade
@app.get("/events/modality/{modality}", tags=["Events"])
def filtro_modality(modality: str):
    dados = load_events()
    
    eventos_encontrados = []
    
    for evento in dados.get("events", []):
        
        if evento.get("modality") and evento.get("modality").lower() == modality.lower():
            eventos_encontrados.append(evento)
            

    if not eventos_encontrados:
        raise HTTPException(status_code=404, detail="Nenhum evento encontrado.")

    return eventos_encontrados

# por serviço
@app.get("/events/source/{source}", tags=["Events"])
def filtro_source(source: str):
    dados = load_events()
    
    eventos_encontrados = []
    
    for evento in dados.get("events", []):
        
        if evento.get("source") and evento.get("source").lower() == source.lower():
            eventos_encontrados.append(evento)
            

    if not eventos_encontrados:
        raise HTTPException(status_code=404, detail="Nenhum evento encontrado.")

    return eventos_encontrados

# por url
@app.get("/events/url/{url}")
def filtro_url(url: str):
    dados = load_events()
    
    eventos_encontrados = []
    
    for evento in dados.get("events", []):
        
        if evento.get("url") and evento.get("url").lower() == url.lower():
            eventos_encontrados.append(evento)
            

    if not eventos_encontrados:
        raise HTTPException(status_code=404, detail="Nenhum evento encontrado.")

    return eventos_encontrados

# por start_date
@app.get("/events/start_date/{start_date}")
def filtro_start_date(start_date: str):
    dados = load_events()
    
    eventos_encontrados = []
    
    for evento in dados.get("events", []):
        
        if evento.get("start_date") and evento.get("start_date").lower() == start_date.lower():
            eventos_encontrados.append(evento)
            

    if not eventos_encontrados:
        raise HTTPException(status_code=404, detail="Nenhum evento encontrado.")

    return eventos_encontrados
