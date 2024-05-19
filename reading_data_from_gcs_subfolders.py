import pathlib
import google.cloud.storage as gcs

import os
os.environ["GCLOUD_PROJECT"] = "chrome-plateau-393918"

client = gcs.Client()

#set target file to write to
target = pathlib.Path("local_file.txt")

#set file to download
FULL_FILE_PATH = "gs://firstp1/firstp2/pd/sales_data.csv"

#open filestream with write permissions
with target.open(mode="wb") as downloaded_file:
        client.download_blob_to_file(FULL_FILE_PATH, downloaded_file)