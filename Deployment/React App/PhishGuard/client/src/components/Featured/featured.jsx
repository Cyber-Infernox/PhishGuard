import { useState, useEffect } from "react";
import "./featured.scss";

import getURLTypeAPI from "../../api/getURLTypeAPI";
import getModelResultAPI from "../../api/getModelResultAPI";
// import datasetAPI from "../../api/datasetAPI";

const Featured = () => {
  const [search, setSearch] = useState("");
  const [isSearching, setIsSearching] = useState(false);
  const [result, setIsResult] = useState("Detect");

  function checkUrl(url) {
    // Check if the URL does not start with "http://" or "https://"
    if (!url.startsWith("http://") && !url.startsWith("https://")) {
      alert(
        "Please enter a valid URL that starts with 'http://' or 'https://'"
      );
      return false;
    }

    // // Check for "http://www." or "https://www." at the beginning and remove "www."
    // if (url.startsWith("http://www.")) {
    //   url = "http://" + url.substring(11); // Keep "http://" and remove "www."
    // } else if (url.startsWith("https://www.")) {
    //   url = "https://" + url.substring(12); // Keep "https://" and remove "www."
    // }

    // console.log("Valid URL (without 'www.'):", url);
    return true;
  }

  useEffect(() => {
    // Set a timer to reset the result to "Detect" after 10 seconds
    const timer = setTimeout(() => {
      setIsResult("Detect");
    }, 7000); // 10,000 milliseconds = 10 seconds

    // Cleanup function to clear the timer if the component unmounts or result changes
    return () => {
      clearTimeout(timer);
    };
  }, [result]); // Depend on `result` to reset timer when `result` changes

  const handleDetect = async () => {
    if (!checkUrl(search)) {
      // If the URL is invalid, stop further execution
      return;
    }

    setIsSearching(true); // Indicate loading or processing
    try {
      // var response = await getURLTypeAPI(search);
      // console.log(response);

      // if (response.data === null) {
      // const newURL = checkUrl(search);
      // console.log("Updated URL:", newURL);
      const response = await getModelResultAPI(search);

      //   const data = {
      //     url: search,
      //     type: response.data,
      //   };

      //   await datasetAPI(data);
      //   alert("Added to database successfully!");
      if (response.message && response.message === "Network Error")
        setIsResult("PHISHING");
      else setIsResult(response);
      console.log("API response:", response);
      // } else {
      //   console.log("Got from database");
      //   setIsResult(response.data);
      //   console.log("API response:", response.data);
      // }
    } catch (err) {
      console.error("Error in detection:", err);
      alert("An unexpected error occurred while detecting URL type.");
    } finally {
      setIsSearching(false); // Reset loading or processing state
    }
  };

  return (
    <div className="featured">
      <div className="container">
        <div className="left">
          <h1>YOUR TRUSTED PHISHING DETECTION PLATFORM</h1>
          <div className="search">
            <div className="searchInput">
              <img
                className="searchIcon"
                src="./media/search.png"
                alt="search"
              />
              <input
                type="search"
                placeholder={"Paste any URL"}
                value={search}
                onChange={({ target: { value } }) =>
                  setSearch(value.toLowerCase())
                }
                aria-label="Search input" // Improve accessibility
              />
            </div>
            <button
              onClick={handleDetect}
              disabled={isSearching} // Disable button if empty or processing
            >
              {isSearching ? "Detecting..." : result}
            </button>
          </div>
        </div>

        <div className="right">
          <img src="./media/security2.jpg" alt="hero" />
        </div>
      </div>
    </div>
  );
};

export default Featured;
