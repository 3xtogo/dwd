import urllib.request
import urllib.parse
from ics import Calendar  # , Event


class ConnectedCalenar:
    reference = 'https://icspy.readthedocs.io/en/stable/'

    def __init__(self, url):
        """

        :param url: url to ics
        """
        self.calendar = Calendar()
        self.url = url

        self.fetch()

    def fetch(self):
        self.calendar = Calendar(self.fetchIcsFromWeb(self.url))

    def eventsList(self):
        ls = []
        for ev in self.calendar.events:
            print(ev.begin, ev.end, '\n\t', ev.name, '\n\t', ev.location, '\n')
            ls.append({'begin': ev.begin, 'end': ev.end, 'name': ev.name, 'loc': ev.location})
        return ls

    @staticmethod
    def fetchIcsFromWeb(url):
        """

        :param url: download ics
        :return: string ics
        """
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        icalStr = the_page.decode('UTF-8')
        return icalStr


if __name__ == '__main__':
    myUrl = 'https://studip.hs-rm.de/dispatch.php/ical/index/qz8Lhst2'
    myCal = ConnectedCalenar(myUrl)
    myCal.eventsList()
