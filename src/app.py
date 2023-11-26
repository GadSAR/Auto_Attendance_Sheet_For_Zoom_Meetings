# TODO: This file not needed for now. run script instead from /src/scripts
from src.controllers.rest_controller import RestAPI

app = RestAPI().app

if __name__ == '__main__':
    app.run()
