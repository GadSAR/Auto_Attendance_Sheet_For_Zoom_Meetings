import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "ZOOM_MEETING_ID": os.getenv("ZOOM_MEETING_ID"),
    "ZOOM_MEETING_PASSWORD": os.getenv("ZOOM_MEETING_PASSWORD"),
    "ZOOM_MEETING_NAME": os.getenv("ZOOM_MEETING_NAME"),
    "GOOGLE_SHEETS_URL": os.getenv("GOOGLE_SHEETS_URL"),
}
