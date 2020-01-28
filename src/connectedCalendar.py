import urllib.request
import urllib.parse
from ics import Calendar, Event


# using ics
# https://icspy.readthedocs.io/en/stable/

class myCalendar:
    def __init__(self, url):
        """

        :param kwargs: url
        """
        self.calendar = Calendar()
        self.url = url

    @staticmethod
    def fetchIcsFromWeb(url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        icalStr = the_page.decode('UTF-8')
        return icalStr







if __name__ == '__main__':

    myUrl = 'https://studip.hs-rm.de/dispatch.php/ical/index/qz8Lhst2'
    myCalendar(myUrl)
    1
