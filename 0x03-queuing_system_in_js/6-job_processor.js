// import kue from kue
import kue from 'kue';
// create a queue instance
const queue = kue.createQueue();
// Create a function to create notifications
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
// Create a function to push the notification code
queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
})
