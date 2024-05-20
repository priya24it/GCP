#gcloud run deploy pubsub-tutorial --image REGION-docker.pkg.dev/PROJECT_ID/REPOSITORY/pubsub  --no-allow-unauthenticated

from google.cloud import pubsub_v1
import subprocess
project = "gcloud run deploy pubsub-tutorial --image us-east5-docker.pkg.dev/chrome-plateau-393918/repsample/pubsub  --region=us-east5  --no-allow-unauthenticated"
return_value = subprocess.call(project, shell=True)
print(return_value)
if return_value == 0:
    print("Dep app ==> has created successfully..")
else:
    print("error")
    
# Service URL: https://pubsub-tutorial-ta76g6xb3a-ul.a.run.app