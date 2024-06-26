import axios from "axios";

const reportAPI = async (data) => {
  const { url, description, observation } = data;
  // console.log(data);
  return await axios
    .post("https://phish-server.onrender.com/api/db/report/", {
      // .post(`${process.env.REACT_APP_SERVER_URL}api/db/report/`, {
      url,
      description,
      observation,
    })
    .then((res) => {
      console.log(res.data);
      return res.data;
    })
    .catch((err) => {
      return { success: false, message: err.message };
    });
};

export default reportAPI;
