import "./SearchBar.css";

function SearchBar() {
    return (
        <section className="search">

            <input
                type="text"
                placeholder="🔍 Pesquise por evento, cidade ou tecnologia..."
            />

            <button>
                Buscar
            </button>

        </section>
    );
}

export default SearchBar;