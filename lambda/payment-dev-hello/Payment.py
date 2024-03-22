import pika
import json
import uuid

queue_payment_request = 'paymentRequest'
queue_payment_response = 'paymentResponse'

def on_message(channel, method, properties, body):
    try:
        print("Received payment request")
        payment_request_id = body.decode('utf-8')
        print("Payment id requested:", payment_request_id)

        payment_confirmation_id = str(uuid.uuid4())
        print("Generated payment confirmation id:", payment_confirmation_id)
        
        output_message = {
            "paymentRequestId": payment_request_id,
            "paymentConfirmationId": payment_confirmation_id
        }
        
        json_data = json.dumps(output_message)
        
        output_bytes = json_data.encode('utf-8')

        # Publish the response to the paymentResponse queue
        channel.basic_publish(exchange='', routing_key=queue_payment_response, body=output_bytes)
        print("Sent payment response:", output_message)

        # Acknowledge the message after successful processing
        # channel.basic_ack(delivery_tag=method.delivery_tag)
        print("Acknowledged payment request")

    except Exception as e:
        print("Error occurred:", str(e))

def handler(event, context):
    try:
        url = f"amqps://ticketuser:ticketpassword@b-4c111b25-7e10-4516-a8bd-e64cdc57e3cb.mq.eu-central-1.amazonaws.com:5671"
        parameters = pika.URLParameters(url)

        connection = pika.BlockingConnection(parameters)
        print("Connected to RabbitMQ")
        channel = connection.channel()
        print("Channel created")

        channel.queue_declare(queue=queue_payment_request, durable=True)
        print("Queue declared")

        channel.basic_consume(queue=queue_payment_request, on_message_callback=on_message, auto_ack=True)
        print("Waiting for messages...")

        # Start consuming messages
        channel.start_consuming()

    except KeyboardInterrupt:
        print("Stopping consumer...")
        channel.stop_consuming()

    finally:
        connection.close()  # Ensure that the connection is closed properly
