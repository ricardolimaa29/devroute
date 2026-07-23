from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers.events import router as events_router


app = FastAPI(
    title="DevRoute API",
    description=(
        "Agrega eventos de tecnologia do Brasil a partir de múltiplas fontes "
        "(feeds estruturados e scrapers best-effort) e retorna em JSON."
    ),
    version="1.0.0",
)


@app.get("/health")
def saude_da_API():
    return {
        "status": "Ok",
        "version": "1.0.9"
}


app.include_router(events_router)
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

