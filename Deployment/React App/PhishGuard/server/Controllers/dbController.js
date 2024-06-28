require("dotenv").config();
const { MongoClient } = require("mongodb");

const Report = require("../Models/dbReport");
const Dataset = require("../Models/dbDataset");

// Report URL
const reportURL = async (req, res) => {
  const newReport = new Report(req.body);

  try {
    const savedReport = await newReport.save();
    res.status(200).json(savedReport);
  } catch (err) {
    console.log(err);
  }
};

// Dataset URL
const datasetURL = async (req, res) => {
  const newData = new Dataset(req.body);

  try {
    const savedData = await newData.save();
    res.status(200).json(savedData);
  } catch (err) {
    console.log(err);
  }
};

// Get URL type
const typeURL = async (req, res) => {
  const url = req.body.url;

  const client = new MongoClient(process.env.MONGO_URI);

  try {
    await client.connect();
    const db = client.db(process.env.MONGO_PREDICT_DB);
    const collection = db.collection(process.env.MONGO_PREDICT_COLLECTION);

    const result = await collection.findOne({ url: url });
    res.status(200).json(result ? result.type : null);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Internal Server Error" });
  } finally {
    await client.close();
  }
};

module.exports = { reportURL, datasetURL, typeURL };
