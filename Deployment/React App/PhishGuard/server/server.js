require("dotenv").config();

const express = require("express");
const cors = require("cors");
const mongoose = require("mongoose");
const dbRoutes = require("./Routes/db");

// express app
const app = express();

// middleware
app.use(
  cors({
    origin: "https://phish-guard.vercel.app", // Replace with your client app's origin
  })
);
app.use(express.json()); // For POST and PATCH requests
app.use((req, res, next) => {
  console.log(req.path, req.method);
  next();
});

// routes
app.use("/api/db", dbRoutes);

// connect to database
mongoose
  .connect(process.env.MONGO_URI)
  .then(() => {
    // listen for requests
    app.listen(process.env.PORT, () => {
      console.log("Connected to database");
    });
  })
  .catch((error) => {
    console.log(error);
  });
