import axios from "axios";

const reportAPI = async (data) => {
  const { url, description, observation } = data;
  // console.log(data);
  console.log("ENV = " + process.env.REACT_APP_SERVER_URL);
  return await axios
    .post(`${process.env.REACT_APP_SERVER_URL}api/db/report/`, {
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
