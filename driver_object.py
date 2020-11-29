from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
# from seleniumwire import webdriver 
import settings


class Selenium_object:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("--start-maximized")
        # options.headless = True
        # path = r'C:\Users\Administrator\PycharmProjects\GoogleAdsTest\chrome-data'
        # self.chrome_options.add_argument(f"--user-data-dir={path}")
        # self.chrome_options.add_argument("--disable-gpu")
        # self.chrome_options.add_argument("--disable-notifications")
        # self.chrome_options.add_argument('--no-sandbox')
        # self.chrome_options.add_argument('--verbose')
        # self.chrome_options.add_argument('--disable-dev-shm-usage')
        # self.chrome_options.add_experimental_option("prefs", {
        #     "download.default_directory": r"C:\Users\Administrator\PycharmProjects\GoogleAdsTest",
        #     "download.prompt_for_download": False,
        #     "download.directory_upgrade": True,
        #     "safebrowsing_for_trusted_sources_enabled": True,
        #     "safebrowsing.enabled": True
        # })

        self.driver = webdriver.Chrome(executable_path=settings.path_to_driver, options=self.chrome_options)
        self.driver.implicitly_wait(30)
        self.wait = WebDriverWait(self.driver, 30)