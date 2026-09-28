import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.ini')
config.read(config_path)

class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common_info', 'baseURL')
        return url

    @staticmethod
    def get_browser():
        browser = config.get('common_info', 'browser')
        return browser
