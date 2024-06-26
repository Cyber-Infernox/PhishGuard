import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./pages/Home/home";
import Footer from "./pages/Footer/Footer";
import Navbar from "./components/Navbar/navbar";
import "./App.scss";

function App() {
  const Layout = ({ children }) => {
    return (
      <div>
        <Navbar />
        {children}
        <Footer />
      </div>
    );
  };

  return (
    <Router>
      <Routes>
        <Route
          path="/"
          element={
            <Layout>
              <Home />
            </Layout>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
