import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

#用在utils
DOWNLOADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos') #到DOWNLOADS_DIR創一個資料夾,名稱叫videos
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
