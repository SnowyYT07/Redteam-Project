const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/');
  },
  filename: function (req, file, cb) {
    const ext = path.extname(file.originalname);
    cb(null, `${Date.now()}-${file.originalname}`);
  }
});

const upload = multer({ storage });

app.post('/upload', upload.single('file'), (req, res) => {
  if(!req.file) {
    console.log("Select a file to upload");
    return res.status(400).send("No file selected for upload");
  }

  console.log("File with name: '${req.file.originalname}' sucessefuly recieved ");
  return res.status(200).send("File uploaded");
});

app.use('/uploads', express.static('uploads'));

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
  
