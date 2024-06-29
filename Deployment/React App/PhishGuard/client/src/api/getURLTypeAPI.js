import axios from "axios";

const getURLTypeAPI = async (url) => {
  try {
    const response = await axios.post(
      `${process.env.REACT_APP_SERVER_URL}api/db/type/`,
      {
        url,
      }
    );
    return response;
  } catch (err) {
    console.error("Error while fetching URL type:", err);
    return { success: false, message: err.message };
  }
};

export default getURLTypeAPI;
