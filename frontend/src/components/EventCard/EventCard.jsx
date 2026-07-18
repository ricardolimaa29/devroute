import "./EventCard.css";

function EventCard({
    titulo,
    cidade,
    estado,
    data,
    categoria,
    modalidade,
    url
}) {

    return (

        <div className="card">

            <div className="badge">
                {categoria}
            </div>

            <h2>{titulo}</h2>

            <p>

                📍 {cidade} - {estado}

            </p>

            <p>

                📅 {data}

            </p>

            <p>

                💻 {modalidade}

            </p>

            <a
                href={url}
                target="_blank"
                rel="noreferrer"
            >
                <button>

                    Ver Evento

                </button>
            </a>

        </div>

    );

}

export default EventCard;