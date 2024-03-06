import { v4 as uuidv4 } from 'uuid';
import * as amqp from 'amqplib/callback_api.js';

const queuePaymentRequest = 'paymentRequest';
const queuePaymentResponse = 'paymentResponse';

amqp.connect('amqps://ticketuser:ticketpassword@b-4c111b25-7e10-4516-a8bd-e64cdc57e3cb.mq.eu-central-1.amazonaws.com:5671', function (error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function (error1, channel) {
        if (error1) {
            throw error1;
        }

        channel.assertQueue(queuePaymentRequest, { durable: true });
        channel.assertQueue(queuePaymentResponse, { durable: true });
        channel.consume(queuePaymentRequest, function (inputMessage) {
            var paymentRequestId = inputMessage.content.toString();
            var paymentConfirmationId = uuidv4();
            console.log("\n\n [x] Received payment request %s", paymentRequestId);
            var outputMessage = '{"paymentRequestId": "' + paymentRequestId + '", "paymentConfirmationId": "' + paymentConfirmationId + '"}';
            channel.sendToQueue(queuePaymentResponse, Buffer.from(outputMessage));
            console.log(" [x] Sent payment response %s", outputMessage);
        }, {
            noAck: true
        });
    });
});
