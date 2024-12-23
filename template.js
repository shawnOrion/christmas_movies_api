const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000; // Use process.env.PORT for Heroku

// Middleware to parse JSON and enable CORS
app.use(express.json());

// CORS configuration
app.use(cors({
    origin: 'https://canvas.play.rosebud.ai', // Allow requests from this origin
    methods: ['GET', 'POST', 'PUT', 'DELETE'], // Allowed HTTP methods
    allowedHeaders: ['Content-Type', 'Authorization'], // Allowed headers
}));

// Start the server
app.listen(PORT, () => {
    console.log(`Movies backend is running on http://localhost:${PORT}`);
});
