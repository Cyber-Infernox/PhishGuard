import axios from "axios";

const datasetAPI = async (data) => {
  const { url, type } = data;
  // console.log(data);
  return await axios
    .post(`${process.env.REACT_APP_SERVER_URL}api/db/dataset/`, {
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
