const express = require('express');
const multer = require('multer');
const path = require('path');
const { spawn } = require('child_process');

const app = express();
const port = 3000;

// Set up storage for uploaded files
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, 'uploads/');
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  }
});

const upload = multer({ storage: storage });

// Ensure the uploads directory exists
const fs = require('fs');
if (!fs.existsSync('uploads')) {
  fs.mkdirSync('uploads');
}

app.post('/predictparkinsons', upload.single('audio'), (req, res) => {
  const filePath = path.join(__dirname, 'uploads', req.file.filename);

  // Call Python script for feature extraction
  const pythonProcess = spawn('python', ['FeatureExtraction.py', filePath]);

  let dataToSend = "";
  pythonProcess.stdout.on('data', (data) => {
    dataToSend += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  pythonProcess.on('close', (code) => {
    if (code !== 0) {
      res.status(500).send("Error in feature extraction");
    } else {
      res.json(JSON.parse(dataToSend));
    }
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
