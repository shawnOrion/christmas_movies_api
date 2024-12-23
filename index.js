const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;

// Middleware to parse JSON and enable CORS
app.use(express.json());
app.use(cors());

// Load movies data into memory
const moviesFilePath = path.join(__dirname, 'data', 'christmas_movies.json');
let movies = [];

// Read and parse movies data
try {
    const moviesData = fs.readFileSync(moviesFilePath, 'utf-8');
    movies = JSON.parse(moviesData);
    console.log(`Loaded ${movies.length} movies into memory.`);
} catch (error) {
    console.error('Error loading movies data:', error.message);
}

// API Endpoint to get movies data
app.get('/api/movies', (req, res) => {
    try {
        res.status(200).send(movies);
    } catch (error) {
        console.error('Error serving movies data:', error.message);
        res.status(500).send({ error: 'Failed to retrieve movies data.' });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Movies backend is running on http://localhost:${PORT}`);
});