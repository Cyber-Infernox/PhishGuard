require("dotenv").config();
const mongoose = require("mongoose");
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
  const url = req.body.url; // You need to specify the property 'url'

  const client = new MongoClient(process.env.MONGO_URI);

  try {
    await client.connect(); // Connect to the MongoDB client
    const db = client.db(process.env.MONGO_PREDICT_DB); // Get the database
    const collection = db.collection(process.env.MONGO_PREDICT_COLLECTION); // Get the collection

    const result = await collection.findOne({ url: url }); // Find a document with the specified URL
    res.status(200).json(result ? result.type : null); // Return the type or null if not found
  } catch (err) {
    console.error(err); // Log errors to the console
    res.status(500).json({ error: "Internal Server Error" }); // Send a server error response
  } finally {
    await client.close(); // Ensure client is closed
  }
};

module.exports = { reportURL, datasetURL, typeURL };
