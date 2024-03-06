// Start by importing kue from kue
import kue from 'kue';
// create an instance of queue
const queue = kue.createQueue();
// Creat a job object
const job = {
	    phoneNumber: 'string',
	    message: 'string',
};
// Log the message to the console depending on the condition
const pushCode = queue.create('push_notification_code', job).save((err) => {
  if (!err) console.log(`Notification job created: ${pushCode.id}`);
  }
);

pushCode.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
