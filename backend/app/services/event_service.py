from math import ceil

from repositories.event_repository import EventRepository


class EventService:

    @staticmethod
    def get_all_events():

        return EventRepository.load_events()

    @staticmethod
    def get_by_id(event_id: int):

        eventos = EventRepository.load_events()

        for evento in eventos:

            if evento.get("id") == event_id:

                return evento

        return None

    @staticmethod
    def list_events(
        page=1,
        limit=20,
        search=None,
        state=None,
        category=None,
        modality=None,
        status=None,
    ):

        eventos = EventRepository.load_events()

        if search:

            texto = search.lower()

            eventos = [

                evento

                for evento in eventos

                if (
                    texto in evento.get("title", "").lower()
                    or texto in evento.get("city", "").lower()
                    or texto in evento.get("state", "").lower()
                    or texto in evento.get("category", "").lower()
                    or texto in evento.get("modality", "").lower()
                )

            ]

        if state:

            eventos = [

                evento

                for evento in eventos

                if evento.get("state", "").lower() == state.lower()

            ]

        if category:

            eventos = [

                evento

                for evento in eventos

                if evento.get("category", "").lower() == category.lower()

            ]

        if modality:

            eventos = [

                evento

                for evento in eventos

                if evento.get("modality", "").lower() == modality.lower()

            ]

        total = len(eventos)

        pages = ceil(total / limit) if total else 1

        inicio = (page - 1) * limit

        fim = inicio + limit

        return {

            "items": eventos[inicio:fim],

            "page": page,

            "limit": limit,

            "total": total,

            "pages": pages,

            "has_next": page < pages,

            "has_previous": page > 1,

        }