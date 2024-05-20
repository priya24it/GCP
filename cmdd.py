import subprocess
import os
os.environ["GOOGLE_CLOUD_PROJECT"] = 'chrome-plateau-393918'
print(os.environ["GOOGLE_CLOUD_PROJECT"])


#=======================================
# Create the artifact reg
# project = "gcloud artifacts repositories create rep_sample \
#     --repository-format=docker \
#     --location=us-east5"
# return_value = subprocess.call(project, shell=True)
# print(return_value)
#============================================

# project = "gcloud info"
# project = "gcloud config list"
# project = "gcloud config set project chrome-plateau-393918"
# project = "gcloud auth application-default login --no-launch-browser"

# result = subprocess.run(["gcloud config list"], shell=True, capture_output=True, text=True)
# result = subprocess.call(["gcloud config list"], shell=True)
# subprocess.call(["gcloud config list"], shell=True)
# print(result.stdout)

