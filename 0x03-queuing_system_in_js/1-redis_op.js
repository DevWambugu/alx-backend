// import redis
import { createClient, print } from "redis";
// Create a server client
const server_client = createClient();

server_client
  .on("connect", () => {
	      console.log("Redis client connected to the server");
	    })
  .on("error", (error) => {
	      console.log(`Redis client not connected to the server: ${error}`);
	    });
// Write a function that creates a new school
function setNewSchool(schoolName, value) {
	  server_client.set(schoolName, value, print);
}
//write a function that displays the school values
function displaySchoolValue(schoolName) {
	  server_client.get(schoolName, (error, result) => {
		      if (error) {
			            console.log(error);
			            throw error;
			          }
		      console.log(result);
		    });
}
// Call the functions to display the output
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
