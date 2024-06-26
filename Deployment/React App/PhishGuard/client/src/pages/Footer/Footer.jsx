import { useEffect } from "react";
import "./footer.scss";

const Footer = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  return (
    <div className="footer">
      <div className="container">
        <div className="bottom">
          <div className="left">
            <h2>PhishGuard</h2>
            <span>© PhishGuard Private Ltd. {new Date().getFullYear()}</span>
          </div>
          <div className="right">
            <div className="social">
              <img src="./media/twitterx2.png" alt="" />
              <img src="./media/facebook.png" alt="" />
              <img src="./media/linkedin.png" alt="" />
              <img src="./media/pinterest.png" alt="" />
              <img src="./media/instagram.png" alt="" />
            </div>
            <div className="link">
              <img src="./media/language.png" alt="" />
              <span>English</span>
            </div>
            <div className="link">
              <img src="./media/accessibility.png" alt="" />
              <span>INR</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Footer;
