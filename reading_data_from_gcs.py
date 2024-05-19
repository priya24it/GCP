
from io import BytesIO
from google.cloud import storage
import pandas as pd
import google.auth

import os
os.environ["GCLOUD_PROJECT"] = "chrome-plateau-393918"

project_id = google.auth.default()

bucket_name = 'firstb3'
blob_name = "sales_data.csv"

storage_client = storage.Client()
bucket = storage_client.bucket(bucket_name)
blob = bucket.blob(blob_name)
s = blob.download_as_string()
print(s)
