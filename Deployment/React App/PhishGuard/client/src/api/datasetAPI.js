import axios from "axios";

const datasetAPI = async (data) => {
  const { url, type } = data;
  // console.log(data);
  return await axios
    .post("https://phish-server.onrender.com/api/db/dataset/", {
      // .post(`${process.env.REACT_APP_SERVER_URL}api/db/report/`, {
      url,
      type,
    })
    .then((res) => {
      console.log(res.data);
      return res.data;
    })
    .catch((err) => {
      return { success: false, message: err.message };
    });
};

export default datasetAPI;
