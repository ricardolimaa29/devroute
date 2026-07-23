from fastapi import APIRouter, HTTPException, Query

from services.event_service import EventService

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.get("/")
def get_events(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=20, ge=1, le=20),

    search: str | None = None,
    state: str | None = None,
    category: str | None = None,
    modality: str | None = None,
    status: str | None = None,
):

    return EventService.list_events(
        page=page,
        limit=limit,
        search=search,
        state=state,
        category=category,
        modality=modality,
        status=status,
    )


@router.get("/{id}")
def filtro_id(id: int):

    evento = EventService.get_by_id(id)

    if evento is None:

        raise HTTPException(
            status_code=404,
            detail="Evento não encontrado"
        )

    return evento

@router.get("/city/{city}")
def filtro_city(city: str):

    eventos = EventService.get_all_events()

    resultado = [
        evento
        for evento in eventos
        if evento.get("city")
        and evento["city"].lower() == city.lower()
    ]

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Nenhum evento encontrado para esta cidade."
        )

    return resultado


@router.get("/state/{state}")
def filtro_state(state: str):

    eventos = EventService.get_all_events()

    resultado = [
        evento
        for evento in eventos
        if evento.get("state")
        and evento["state"].lower() == state.lower()
    ]

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Nenhum evento encontrado para este estado."
        )

    return resultado


@router.get("/modality/{modality}")
def filtro_modality(modality: str):

    eventos = EventService.get_all_events()

    resultado = [
        evento
        for evento in eventos
        if evento.get("modality")
        and evento["modality"].lower() == modality.lower()
    ]

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Nenhum evento encontrado."
        )

    return resultado


@router.get("/source/{source}")
def filtro_source(source: str):

    eventos = EventService.get_all_events()

    resultado = [
        evento
        for evento in eventos
        if evento.get("source")
        and evento["source"].lower() == source.lower()
    ]

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Nenhum evento encontrado."
        )

    return resultado


@router.get("/url/{url:path}")
def filtro_url(url: str):

    eventos = EventService.get_all_events()

    resultado = [
        evento
        for evento in eventos
        if evento.get("url")
        and evento["url"].lower() == url.lower()
    ]

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Nenhum evento encontrado."
        )

    return resultado


@router.get("/start_date/{start_date}")
def filtro_start_date(start_date: str):

    eventos = EventService.get_all_events()

    resultado = [
        evento
        for evento in eventos
        if evento.get("start_date")
        and evento["start_date"].lower() == start_date.lower()
    ]

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Nenhum evento encontrado."
        )

    return resultado