require('dotenv').config();
const express = require('express');
const redis = require('redis');
const shortid = require('shortid');

const app = express();
app.use(express.json());

const PORT = process.env.PORT || 3000;

const redisClients = [

//     redis.createClient({ host: process.env.REDIS_HOST_1, port: process.env.REDIS_PORT_1 }),
//   redis.createClient({ host: process.env.REDIS_HOST_2, port: process.env.REDIS_PORT_2 }),
//   redis.createClient({ host: process.env.REDIS_HOST_3, port: process.env.REDIS_PORT_3 })
  redis.createClient({ socket: { host: process.env.REDIS_HOST_1, port: Number(process.env.REDIS_PORT_1) } }),
  redis.createClient({ socket: { host: process.env.REDIS_HOST_2, port: Number(process.env.REDIS_PORT_2) } }),
  redis.createClient({ socket: { host: process.env.REDIS_HOST_3, port: Number(process.env.REDIS_PORT_3) } })
];

// Hash function to distribute keys among Redis clients
function getRedisClient(key) {
  const hash = key.split('').reduce((acc, char) => acc + char.charCodeAt(0), 0);
  return redisClients[hash % redisClients.length];
}

// Endpoint to shorten a URL with expiration
app.post('/shorten', async (req, res) => {
    const { url, ttl } = req.body; // ttl (time-to-live) is optional
    if (!url) return res.status(400).send('URL is required');
  
    const shortId = shortid.generate();
    const redisClient = getRedisClient(shortId);
  
    try {
      await redisClient.set(shortId, url, { EX: ttl || 3600 }); // Default TTL of 1 hour
      res.json({ shortUrl: `http://localhost:${PORT}/${shortId}` });
    } catch (err) {
      res.status(500).send('Failed to save URL');
    }
  });

// Endpoint to retrieve the original URL with cache metrics
app.get('/:shortId', async (req, res) => {
  const { shortId } = req.params;
  const redisClient = getRedisClient(shortId);

  try {
    const url = await redisClient.get(shortId);
    if (!url) {
      console.log(`Cache miss for key: ${shortId}`);
      return res.status(404).send('URL not found');
    }
    console.log(`Cache hit for key: ${shortId}`);
    return res.redirect(url);
  } catch (err) {
    return res.status(500).send('Server error');
  }
});

async function start() {
  try {
    await Promise.all(redisClients.map(c => c.connect()));
    app.listen(PORT, () => {
      console.log(`Server running on port ${PORT}`);
    });
  } catch (err) {
    console.error('Failed to connect to Redis:', err);
    process.exit(1);
  }
}

start();