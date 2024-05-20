

# Create the artifact reg

import subprocess
path = r'C:\\pubsub\\pythonProject2\\python-docs-samples\\run\\pubsub'
project = f"gcloud builds submit --tag us-east5-docker.pkg.dev/chrome-plateau-393918/repsample/pubsub {path}"
return_value = subprocess.call(project, shell=True)
print(return_value)
if return_value == 0:
    print("Build your container and publish on Artifact Registry: ==> has created successfully..")
else:
    print("error")