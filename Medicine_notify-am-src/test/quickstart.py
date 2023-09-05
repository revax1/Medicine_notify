import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# สร้างฟังก์ชันเพื่อรับรายการรับรอง
def get_credentials(user_folder):
    creds = None
    token_path = f'token_{user_folder}.pickle'
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token:
            creds = pickle.load(token)
    return creds

# สร้างบริการ Google Drive
def create_drive_service(user_folder):
    creds = get_credentials(user_folder)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(f'credentials_{user_folder}.json', ['https://www.googleapis.com/auth/drive'])
        creds = flow.run_local_server(port=0)
        with open(f'token_{user_folder}.pickle', 'wb') as token:
            pickle.dump(creds, token)

    drive_service = build('drive', 'v3', credentials=creds)
    return drive_service

# อัพโหลดไฟล์
def upload_file(user_folder, file_path):
    drive_service = create_drive_service(user_folder)
    file_metadata = {'name': os.path.basename(file_path)}
    media = MediaFileUpload(file_path)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID:', file.get('id'))

# ดาวน์โหลดไฟล์
def download_file(user_folder, file_id, download_path):
    drive_service = create_drive_service(user_folder)
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(download_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    print('File downloaded.')

# ตัวอย่างการใช้งาน
user_folder = 'user1'
file_path = 'database.db'
upload_file(user_folder, file_path)

file_id = 'your_file_id_here'
download_path = 'downloaded_database.db'
download_file(user_folder, file_id, download_path)
