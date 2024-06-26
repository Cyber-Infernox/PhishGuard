const mongoose = require("mongoose");

const Schema = mongoose.Schema;

const newConnection = mongoose.createConnection(process.env.MONGO_URI, {
  dbName: process.env.MONGO_REPORT_DB, // Name of the new database
});

const reportSchema = new Schema(
  {
    url: {
      type: String,
      required: true,
    },
    date: {
      type: Date,
      default: Date.now,
      required: true,
    },
    description: {
      type: String,
    },
    observation: {
      type: String,
    },
  },
  { timestamps: true }
);

// Making model of the above schema
module.exports = newConnection.model("Report", reportSchema, "urls");
