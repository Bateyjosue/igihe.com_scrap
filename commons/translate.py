"""
This script helps translating text from Kiny/English to English/Kiny
"""


class Translate:
    def __init__(self):
        """
        init
        """
        pass 

    def language_detect(self):
        """
        language detect
        """
        raise NotImplementedError

    def english_kiny(self):
        """
        reading csv
        """
        raise NotImplementedError

    def kiny_english(self):
        """
        reading pdf
        """ 
        raise NotImplementedError