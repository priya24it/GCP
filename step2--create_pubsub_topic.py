from google.cloud import pubsub_v1
import google.auth
#
# import os
# os.environ["GCLOUD_PROJECT"] = "chrome-plateau-393918"
# project_id = google.auth.default()

# PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
# TOPIC = f"pubsub-test_{SUFFIX}"
#client = speech.SpeechClient().from_service_account_json('c:/config/service-account.json')

project = "chrome-plateau-393918"
topic = "myRunTopic"
publisher = pubsub_v1.PublisherClient()#.from_service_account_json(r'C:\\Users\\priya\\AppData\\Roaming\\gcloud\\application_default_credentials.json')
topic_path = publisher.topic_path(project, topic)
abc = publisher.create_topic(request={"name": topic_path})
print(abc)