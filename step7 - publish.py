from google.cloud import pubsub_v1
import google.auth
pubsub_topic = 'myRunTopic'
PROJECT = 'chrome-plateau-393918'


# Post the message "Runner" to the topic
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT, pubsub_topic)
message = "Hara Hara Mahadev"
data = message.encode("utf-8")
# When you publish a message, the client returns a future.
future = publisher.publish(topic_path, data)
print(future.result())



