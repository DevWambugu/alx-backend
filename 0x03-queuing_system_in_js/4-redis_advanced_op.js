// Import create client
const { createClient } = require('redis');

// Proceed to creating a REDIS Client
const client = createClient();

// This section handles the redic client errorss
client.on('error', (error) => {
  console.error('Redis client error:', error);
});

// Use hset to store the hash values
client.hset(
  'HolbertonSchools',
  'Portland', 50,
  'Seattle', 80,
  'New York', 20,
  'Bogota', 20,
  'Cali', 40,
  'Paris', 2,
  (error, reply) => {
    if (error) {
      console.error('Error storing hash values:', error);
    } else {
      console.log(reply);
    }
  }
);
