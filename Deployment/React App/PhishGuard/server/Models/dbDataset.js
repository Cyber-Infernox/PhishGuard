const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const newConnection = mongoose.createConnection(process.env.MONGO_URI, {
  dbName: process.env.MONGO_PREDICT_DB, // Name of the new database
});

const datasetSchema = new Schema({
  url: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    required: true,
  },
});

// Making model of the above schema
module.exports = newConnection.model("Dataset", datasetSchema, "urls");
