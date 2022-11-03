"""
This script helps webscraping various websites
"""


class WebScrap:
    """
      Webscrap
    """
    def __init__(self):
        """
        init
        """
        self.info = "Webscrap"

    def get_content(self):
        """
        get web  content
        """
        raise NotImplementedError

    def process_content(self):
        """
        process retrieved web content
        """
        raise NotImplementedError