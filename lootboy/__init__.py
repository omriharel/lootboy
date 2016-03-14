import requests
import re

import lootboy.colors
import lootboy.constants


class Lootboy(object):

    def __init__(self, config=None, target_path=None):
        self._config = config
        self._target_path = target_path

        self._source = None

    def loot(self):
        self._fetch_source()
        self._augment_source(self._process_config())
        self._save_filter()

    def _fetch_source(self):
        print 'Fetching most updated version from the web...',
        response = requests.get(lootboy.constants.Constants.source_url)
        try:
            response.raise_for_status()
        except Exception as error:
            raise SystemExit('Unable to fetch filter: {0}'.format(error))

        print 'Downloaded {0}K.'.format(len(response.text) / 1024)
        self._source = response.text.replace('\r\n', '\n')

    def _process_config(self):
        return '# Oh, just imagine the possibilities...'

    def _augment_source(self, text):
        original_pattern = lootboy.constants.Constants.override_section_start_pattern
        replacement = lambda match: '{0}{1}\n{2}\n{3}'.format(match.group(0),
                                                              lootboy.constants.Constants.lootboy_section_start,
                                                              text,
                                                              lootboy.constants.Constants.lootboy_section_end)

        new_source, occurences = re.subn(original_pattern, replacement, self._source, count=1)

        if occurences != 1:
            raise SystemExit('Error: Lootboy didn\'t find the override section in the given filter!')

        self._source = new_source
        print 'Augmented original loot filter with custom additions.'

    def _save_filter(self):
        with open(self._target_path, 'w') as f:
            f.write(self._source.replace('\n', '\r\n'))

        print 'New filter written to \'{0}\' :)'.format(self._target_path)
