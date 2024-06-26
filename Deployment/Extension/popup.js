// Function to send a POST request to a specified endpoint
function checkUrl(url, callback) {
  // const endpoint = "http://127.0.0.1:8000/url_prediction"; // Private URL
  const endpoint = "https://5237-34-29-190-96.ngrok-free.app/url_prediction"; // Public URL

  // console.log(url);

  // Create the JSON object with the URL to be sent
  const input_data_for_model = {
    url: url,
  };

  // Convert to JSON string
  const input_json = JSON.stringify(input_data_for_model);

  // Send a POST request to the endpoint
  fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: input_json, // Send the JSON data
  })
    .then((response) => response.text()) // Get the response text
    .then((data) => {
      callback(data); // Call the callback with the response text
    })
    .catch((error) => {
      console.error("Error:", error); // Handle errors
      callback("Error"); // Return an error message to the callback
    });
}

// Get the active tab and send the URL for checking
chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
  const activeTabUrl = tabs[0].url;

  checkUrl(activeTabUrl, (result) => {
    if (result === "Internal Server Error") result = "Phishing";

    // Display the result in the popup
    document.getElementById("result").innerText = "Result: " + result;
  });
});
