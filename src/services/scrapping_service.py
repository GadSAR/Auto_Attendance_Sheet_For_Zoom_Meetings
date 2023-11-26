from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class ScrappingService:
    def start_driver(self):
        options = Options()
        # options.add_argument("--headless")
        options.add_argument("--start-fullscreen")
        driver = webdriver.Chrome(options=options)
        driver.get('chrome://settings/')
        driver.execute_script('chrome.settingsPrivate.setDefaultZoom(0.25);')
        return driver

    def prepare_attendance_sheet(self, zoom_meeting_id, zoom_meeting_password,
                                 zoom_meeting_name, sheets_url):
        driver = self.start_driver()
        participants = self.get_zoom_meeting_participants(driver,
                                                          zoom_meeting_id,
                                                          zoom_meeting_password,
                                                          zoom_meeting_name)
        print(participants)
        print(len(participants))
        self.put_participants_in_google_sheets(driver, sheets_url,
                                               participants)
        driver.quit()

    def get_zoom_meeting_participants(self, driver, zoom_meeting_id,
                                      zoom_meeting_password,
                                      zoom_meeting_name):
        driver.implicitly_wait(30)
        zoom_meeting_url = "https://app.zoom.us/wc/" + zoom_meeting_id + "/join"
        driver.get(zoom_meeting_url)
        driver.find_element(By.ID, "input-for-pwd").send_keys(
            zoom_meeting_password)
        driver.find_element(By.ID, "input-for-name").send_keys(
            zoom_meeting_name)
        driver.find_element(By.CLASS_NAME, "preview-join-button").click()
        driver.find_element(By.XPATH,
                            '/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/footer/div[1]/div[2]/div[1]/button').click()
        elements = driver.find_elements(By.CLASS_NAME,
                                        'participants-item-position')

        participants = []
        driver.implicitly_wait(1)
        for participant in elements:
            try:
                participant.find_element(By.CLASS_NAME,
                                         'lazy-icon-icons\/participants-list\/video-on')
                name = participant.find_element(By.CSS_SELECTOR,
                                                '.participants-item__display-name').text
                participants.append(name)
            except:
                pass

        return participants

    # TODO: Make this function more efficient
    def put_participants_in_google_sheets(self, driver, sheets_url,
                                          participants):
        driver.get(sheets_url)
        cellSearcher = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div[7]/div[7]/div[1]/input')
        cellInput = driver.find_element(By.CSS_SELECTOR,
                                        '#t-formula-bar-input > div')

        # TODO: Need to modify values of these variables
        enterCode = "\uE007"
        Rowindex = 2
        ColNameIndex = "H"
        ColCheckboxIndex = "G"
        while True:
            cellSearcher.clear()
            cellSearcher.send_keys(
                "{0}{1}{2}".format(ColNameIndex, Rowindex, enterCode))
            name = cellInput.text
            if name == "":
                break
            for participant in participants:
                if name in participant:
                    cellSearcher.clear()
                    cellSearcher.send_keys("{0}{1}{2}TRUE{2}".format(ColCheckboxIndex, Rowindex, enterCode))
                    break
            Rowindex += 1
