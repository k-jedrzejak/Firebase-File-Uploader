# Firebase File Uploader

This Python script uploads files modified within the last 24 hours from a specified local directory to a Firebase Storage bucket.

## Prerequisites

- **Python**: Make sure you have Python installed on your machine.
- **Firebase Account**: You need a Firebase account and a Firebase project set up.
- **Firebase Admin SDK**: You need to have the Firebase Admin SDK service account key JSON file. You can download this from your Firebase project's settings under "Service accounts".

## Modify the Script
- Set the folder_path to the path of the local directory containing the files you want to upload.
- Set the storageBucket in the initialize_app function to your Firebase Storage bucket URL, typically in the format project-id.appspot.com.

## Usage
- Place the script in the same directory as your firebase_service_account_key.json or provide the correct path to the JSON file.
- Update the script with your folder_path and storageBucket details.
- Run the script using Python: `python upload_files_to_firebase.py`
