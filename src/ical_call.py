import urllib.request
import urllib.parse
from ics import Calendar, Event

# using ics
# https://icspy.readthedocs.io/en/stable/

# insert ical link here
# link = 'https://studip.hs-rm.de/dispatch.php/ical/index/qz8Lhst2'
link1 = 'badurl'

def get_calendar (link):
    try:
        req = urllib.request.Request(link)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        #lst = the_page.decode('UTF-8').split('\r\n')
        icalStr = the_page.decode('UTF-8')
        #for l in lst:
        #    print(l)
        return Calendar(icalStr)

    except:
        print("Unexpected error: bad URL")
        raise

if __name__ == '__main__'

# try get_calendar(link1):