// import kue from kue
import kue from 'kue';
// create a queue instance
const queue = kue.createQueue();
// Create an array of blacklisted numbers
const blacklisted = ['4153518780', '4153518781'];
//Create a send notifications function
function sendNotification(phoneNumber, message, djob, done) {
  if (blacklisted.includes(djob.data.phoneNumber)) {
            return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  djob.progress(0, 50);
  djob.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  return done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
	    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
