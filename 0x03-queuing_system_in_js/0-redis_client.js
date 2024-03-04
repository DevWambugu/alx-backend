//Use import statemnt to import create client
import { createClient } from "redis";
// Create client
const client = createClient();
// Create event listeners
client
  .on("connect", () => {
	      console.log("Redis client connected to the server");
	    })
  .on("error", (error) => {
	      console.log(`Redis client not connected to the server: ${error}`);
	    });
