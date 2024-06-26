const express = require("express");

const router = express.Router();

// Controller function
const {
  reportURL,
  datasetURL,
  typeURL,
} = require("../Controllers/dbController");

// Report URL
router.post("/report", reportURL);

// Dataset URL
router.post("/dataset", datasetURL);

// GET URL type
router.post("/type", typeURL);

module.exports = router;
