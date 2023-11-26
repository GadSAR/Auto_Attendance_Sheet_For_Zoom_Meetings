from flask import Flask, render_template
from flask_cors import CORS

from src.services.scrapping_service import ScrappingService


class RestAPI:
    def __init__(self):
        self.app = Flask(__name__, template_folder='../resources/templates')
        CORS(self.app)
        self.scrappingService = ScrappingService();

        @self.app.route('/')
        def home():
            return render_template('index.html')

        # TODO: Add a route for the attendance sheet
        @self.app.route('/attendance/<zoom_meeting_id>/<zoom_meeting_password>/<zoom_meeting_name>/<sheets_url>')
        def mezhava(zoom_meeting_id, zoom_meeting_password, zoom_meeting_name, sheets_url):
            self.scrappingService.prepare_attendance_sheet(
                zoom_meeting_id, zoom_meeting_password, zoom_meeting_name, sheets_url)
            return render_template('attendance.html')

    def run(self):
        self.app.run(host='0.0.0.0', port=5000)


app = RestAPI().app
