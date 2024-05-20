

from google.cloud import pubsub_v1
import subprocess
#project = "gcloud iam service-accounts create cloud-run-pubsub-invoker --display-name 'Cloud Run Pub/Sub Invoker'"

# step1
# project = "gcloud iam service-accounts create cloud-run-pubsub-invoker"
# return_value = subprocess.call(project, shell=True)
# print(return_value)
# if return_value == 0:
#     print(" Create or select a service account to represent the Pub/Sub subscription identity. ==> has created successfully..")
# else:
#     print("error")
#step1 end .

#step2
# project = "gcloud run services add-iam-policy-binding pubsub-tutorial \
# --member=serviceAccount:cloud-run-pubsub-invoker@chrome-plateau-393918.iam.gserviceaccount.com --region=us-east5 \
# --role=roles/run.invoker"
# return_value = subprocess.call(project, shell=True)
# print(return_value)
# if return_value == 0:
#     print(" Create a Pub/Sub subscription with the service account: ==> has created successfully..")
# else:
#     print("error")
#step2 end .

#step3
# project = "gcloud run services add-iam-policy-binding pubsub-tutorial \
# --member=serviceAccount:cloud-run-pubsub-invoker@chrome-plateau-393918.iam.gserviceaccount.com --region=us-east5 \
# --role=roles/run.invoker"
# return_value = subprocess.call(project, shell=True)
# print(return_value)
# if return_value == 0:
#     print(" Allow Pub/Sub to create authentication tokens in your project: ==> has created successfully..")
# else:
#     print("error")
#step3 end .

#step4
project = "gcloud pubsub subscriptions create myRunSubscription --topic myRunTopic \
--ack-deadline=600 \
--push-endpoint=https://pubsub-tutorial-ta76g6xb3a-ul.a.run.app/ \
--push-auth-service-account=cloud-run-pubsub-invoker@chrome-plateau-393918.iam.gserviceaccount.com"
return_value = subprocess.call(project, shell=True)
print(return_value)
if return_value == 0:
    print(" Allow Pub/Sub to create authentication tokens in your project: ==> has created successfully..")
else:
    print("error")
#step4 end .