import "./Navbar.css";

function Navbar() {
  return (
    <header className="navbar">

      <div className="logo">
        DevRoute
      </div>

      <nav>

        <a href="#">Home</a>

        <a href="#">Eventos</a>

        <a href="#">Sobre</a>

        <a
          href="https://github.com/ricardolimaa29/devroute"
          target="_blank"
          rel="noreferrer"
        >
          GitHub
        </a>

      </nav>

    </header>
  );
}

export default Navbar;