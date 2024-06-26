import axios from "axios";

const getModelResultAPI = async (url) => {
  try {
    const input_data_for_model = {
      url,
    };

    console.log(input_data_for_model);

    // Convert the object to a JSON string
    const inputJson = JSON.stringify(input_data_for_model);

    console.log("InputJSON" + inputJson);

    const response = await axios.post(
      "https://5237-34-29-190-96.ngrok-free.app/url_prediction", // The public URL provided
      inputJson, // Sending JSON as data
      {
        headers: {
          "Content-Type": "application/json", // Setting the content type to JSON
        },
      }
    );

    return response.data; // Return the JSON response data
  } catch (err) {
    console.error("Error while fetching model result:", err);
    return { success: false, message: err.message };
  }
};

export default getModelResultAPI;
