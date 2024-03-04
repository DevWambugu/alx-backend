// import libraries. Use the import keyword
import { createClient, print } from "redis";
import { promisify } from "util";

//Create a Redis Client
const client_server = createClient();
//set up event listeners for Redis Client
client_server
  .on("connect", () => {
	      console.log("Redis client connected to the server");
	    })
  .on("error", (error) => {
	      console.log(`Redis client not connected to the server: ${error}`);
	    });
//Function to set up new school
function setNewSchool(schoolName, value) {
	  client_server.set(schoolName, value, print);
}



const get = promisify(client.get).bind(client_server);

async function displaySchoolValue(schoolName) {
	    const res = await client.get(schoolName).catch((error) => {
		          if (error) {
				          console.log(error);
				          throw error;
				        }
		        });
	    console.log(res);
	  }
//display school value
displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
