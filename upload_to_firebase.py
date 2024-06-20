import os
import uuid
from firebase_admin import credentials, initialize_app, storage
from datetime import datetime, timedelta

# Initialize Firebase
cred = credentials.Certificate('firebase_service_account_key.json')
firebase_app = initialize_app(cred, {"storageBucket": "your_project_id.appspot.com"})
bucket = storage.bucket()

# Path to the folder containing files to be uploaded
folder_path = "/path/to/your/folder"

current_date = datetime.now()
twenty_four_hours_ago = current_date - timedelta(days=1)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    file_mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))

    if file_mod_time > twenty_four_hours_ago:
        print(f"Processing {filename}...")
        destination_blob_name = f"files/{filename}"

        try:
            blob = storage.bucket().blob(destination_blob_name)
            blob.upload_from_filename(file_path)

            custom_token = str(uuid.uuid4())
            metadata = {"firebaseStorageDownloadTokens": custom_token}
            blob.metadata = metadata
            blob.patch()
            print(f"Uploaded {filename} to Firebase Storage.")

        except Exception as e:
            print(f"Failed to upload {filename}: {e}")
    else:
        print(f"Skipping {filename}, not modified in the last 24 hours.")
