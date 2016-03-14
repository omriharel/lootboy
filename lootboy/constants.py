import re

class Constants(object):
    script_source_url = 'http://pastebin.com/raw/Af00CbhA'

    override_section_message = 'Section: ALPHA # GLOBAL OVERRIDE - ADD YOUR OWN RULES'
    override_section_start_pattern = re.compile(re.escape(Constants.override_section_message) + r'.*\n\#-*\n')

    comment = '# '
    lootboy_section_start = comment + 'LOOTBOY BEGIN! :)'
    lootboy_section_end = comment + 'LOOTBOY DONEZO! <3'
