# create a new SNS topic/ SQS Queue client
# lambda handler with the ARN of snsTopic that sends messsage
# give handler permission to publish messages in the topic
# SNS subscribes the consumer lambda to the topic
# lambda handler to consume message from the queue
# output to SNS