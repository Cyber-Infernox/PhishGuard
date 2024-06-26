import { useEffect, useState } from "react";
import Featured from "../../components/Featured/featured";
// import axios from "axios";

import "./home.scss";

import reportAPI from "../../api/reportAPI";

const Home = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const [formData, setFormData] = useState({
    url: "",
    description: "",
    observation: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Make API call to report endpoint
      await reportAPI(formData);
      alert("Report submitted successfully!");
      // Reset form data after successful submission
      setFormData({
        url: "",
        description: "",
        observation: "",
      });
    } catch (error) {
      console.error("Error submitting report:", error);
      alert("Failed to submit report. Please try again later.");
    }
  };

  return (
    <div className="home">
      <Featured />

      <div className="features">
        <div className="container">
          <div className="item">
            <h1>Tap into a global network of protection with PhishGuard</h1>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>Stay One Step Ahead of Cyber Criminals</h6>
            </div>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>
                Effortless Protection Against Phishing Attempts at Your
                Fingertips
              </h6>
            </div>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>PhisGuard is completely free of charge</h6>
            </div>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>Empower Your Online Community</h6>
            </div>
          </div>
          <div className="item">
            <video src="./media/video.mp4" controls></video>
          </div>
        </div>
      </div>

      <div className="features dark" id="about">
        <div className="container">
          <div className="item">
            <h1>Empower, Safeguard & Innovate</h1>
            <p>
              PhishGuard is a cutting-edge web tool dedicated to identifying and
              preventing phishing attacks.
            </p>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>
                Our platform utilizes advanced machine learning algorithms and
                data analysis techniques for URL assessment.
              </h6>
            </div>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>
                Users simply submit a URL for analysis, and our system evaluates
                multiple factors to determine its phishing likelihood.
              </h6>
            </div>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>
                We provide users with a risk score, indicating the probability
                of the URL being a phishing site.
              </h6>
            </div>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>
                Our mission is to offer a simple yet effective tool in the fight
                against fraudulent websites and protect sensitive information.
              </h6>
            </div>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>
                We empower both individuals and organizations to safeguard
                against cyber threats.
              </h6>
            </div>
            <div className="title">
              <img src="./media/checked.png" alt="check" />
              <h6>
                PhishGuard stands as a reliable guardian, enabling users to make
                informed decisions and avoid falling victim to phishing scams.
              </h6>
            </div>
          </div>
          {
            <div className="item">
              <img src="./media/about2.png" alt="About" />
            </div>
          }
        </div>
      </div>

      <div className="features" id="report">
        <div className="container">
          <div className="item">
            <div className="report-section">
              <h1>
                <span
                  className=""
                  style={{ fontFamily: "inherit", fontWeight: "inherit" }}
                >
                  Report - Phish
                </span>
              </h1>

              <form onSubmit={handleSubmit}>
                <div className="form-group">
                  <label htmlFor="url">
                    URL<span>*</span>{" "}
                  </label>
                  <input
                    type="text"
                    id="url"
                    name="url"
                    placeholder="Enter the URL"
                    value={formData.url}
                    onChange={handleChange}
                    required
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="description">Description</label>
                  <textarea
                    id="description"
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                    rows="4"
                  />
                </div>
                <div className="form-group">
                  <label htmlFor="observation">Observation</label>
                  <textarea
                    id="observation"
                    name="observation"
                    value={formData.observation}
                    onChange={handleChange}
                    rows="4"
                  />
                </div>
                <button type="submit">Submit</button>
              </form>
            </div>
          </div>
          <div className="item">
            <img alt="" src="./media/about.png" />
          </div>
        </div>
      </div>

      <div className="features dark" id="contact">
        <div className="container">
          <div className="item">
            <h1>
              <span
                className=""
                style={{ fontFamily: "inherit", fontWeight: "inherit" }}
              >
                Contact Us -
              </span>
            </h1>
            <div className="contact-info">
              <p>
                If you have any questions,feedback or concerns, we would love to
                hear from you! Please feel free to reach out to us using the
                contact information below:
              </p>
              <br />
              <div className="contact-details">
                <p>
                  <strong>Email:</strong>{" "}
                  <a href="sourav.20214056@mnnit.ac.in">
                    contact@phishguard.com
                  </a>
                </p>
                <p>
                  <strong>Phone:</strong> +91-6209057737
                </p>
                <p>
                  <strong>Address:</strong> MNNIT Allahabad, Prayagraj, Uttar
                  Pradesh 211004
                </p>
                <br />
                <p>
                  Our team is dedicated to providing the best possible support
                  and assistance to our users.
                </p>
                <br />
                <p>
                  Thank you for using PhishGuard and helping us in the fight
                  against online fraud!
                </p>
              </div>
            </div>
          </div>

          {
            <div className="item">
              <img src="./media/contacts2.png" alt="About" />
            </div>
          }
        </div>
      </div>
    </div>
  );
};

export default Home;
