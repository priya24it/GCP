# Create the artifact reg

import subprocess

project = "gcloud artifacts repositories create repsample \
    --repository-format=docker \
    --location=us-east5"
return_value = subprocess.call(project, shell=True)
if return_value == 0:
    print("Artifact Registry standard repository to store your container image ==> has created successfully..")
else:
    print("error")