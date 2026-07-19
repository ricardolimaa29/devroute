import "./SearchSection.css";

function SearchSection({
    total,
    search,
    setSearch
}) {

    return (

        <section className="search-section">

            <h2>

                Encontre seu próximo evento

            </h2>

            <input

                type="text"

                placeholder="🔍 Pesquise eventos..."

                value={search}

                onChange={(e)=>setSearch(e.target.value)}

            />

            <div className="filters">

                <select>

                    <option>Todos os estados</option>

                </select>

                <select>

                    <option>Todas as categorias</option>

                </select>

                <select>

                    <option>Todas as modalidades</option>

                </select>

            </div>

            <p>

                {total} eventos encontrados

            </p>

        </section>

    )

}

export default SearchSection;