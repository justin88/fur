from pytabs.config import *

from fur.furApp import FurApp


class FurPyTabsConfiguration(PyTabsConfiguration):

    def __init__(self):
        super().__init__([FurApp])
        self.APPLICATION_ICON_PATH = "fur/resources/fur.png"
        self.APPLICATION_NAME = "Fur"
        self.APPLICATION_CONFIG_FILE_LOCATION = "." + self.APPLICATION_NAME.lower()
        self.WINDOW_TITLE = "Fur"

        self.URL_SCHEME = "fur"
        self.URL_SCHEME_WITH_SEPARATOR = self.URL_SCHEME + '://'

