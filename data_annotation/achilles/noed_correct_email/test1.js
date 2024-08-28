const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

// Replace with your Abstractapi API key
const apiKey = 'YOUR_ABSTRACTAPI_KEY';

app.use(express.json());

app.post('/validate-email', async (req, res) => {
  const { email } = req.body;

  try {
    const response = await axios.get(`https://emailvalidation.abstractapi.com/v1/?api_key=${apiKey}&email=${email}`);

    if (response.data.deliverable) {
      res.json({ valid: true, message: 'Email is valid and deliverable.' });
    } else {
      res.json({ valid: false, message: 'Email is not valid or deliverable.', details: response.data });
    }
  } catch (error) {
    console.error('Error validating email:', error);
    res.status(500).json({ valid: false, message: 'Error validating email.', error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
}); 