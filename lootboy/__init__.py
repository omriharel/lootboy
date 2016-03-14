import requests

import lootboy.colors
import lootboy.consts


class Lootboy(object):

    def __init__(self, config=None):
        self._config = config
        self._source = None

    def loot(self):
        self._fetch_source()
        self._augment_source(self._process_config())
        self._save_filter()
