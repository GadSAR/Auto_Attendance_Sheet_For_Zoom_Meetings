from src.services.scrapping_service import ScrappingService
from src.config import config

zoom_meeting_id = config["ZOOM_MEETING_ID"]
zoom_meeting_password = config["ZOOM_MEETING_PASSWORD"]
zoom_meeting_name = config["ZOOM_MEETING_NAME"]
sheets_url = config["GOOGLE_SHEETS_URL"]
scrappingService = ScrappingService()
scrappingService.prepare_attendance_sheet(
    zoom_meeting_id, zoom_meeting_password, zoom_meeting_name, sheets_url)
