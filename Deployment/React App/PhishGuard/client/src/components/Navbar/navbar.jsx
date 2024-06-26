import { useEffect, useState, React } from "react";
import { Link, useLocation } from "react-router-dom";
import "./navbar.scss";

const Navbar = () => {
  const [showMenu, setShowMenu] = useState(false);
  const { pathname } = useLocation();

  const handleScrollTo = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  const isActive = () => {
    window.scrollY > 0 ? setShowMenu(true) : setShowMenu(false);
  };

  useEffect(() => {
    window.addEventListener("scroll", isActive);
    return () => {
      window.removeEventListener("scroll", isActive);
    };
  }, []);

  return (
    <nav className={showMenu || pathname !== "/" ? "navbar active" : "navbar"}>
      <div className="container">
        <div className="logo">
          <Link to="/" className="link">
            <span className="text">PhishGuard</span>
          </Link>
          <span className="dot">.</span>
        </div>

        <div className="links">
          <div className="menu-links">
            <Link
              to="/#about"
              className="link"
              onClick={() => handleScrollTo("about")}
            >
              About
            </Link>
            <Link
              to="/#report"
              className="link"
              onClick={() => handleScrollTo("report")}
            >
              Report
            </Link>
            <Link
              to="/#contact"
              className="link"
              onClick={() => handleScrollTo("contact")}
            >
              Contact
            </Link>
            <span>English</span>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
