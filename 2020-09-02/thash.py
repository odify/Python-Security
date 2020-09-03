import sys
from optparse import OptionParser
import requests
import re
from bs4 import BeautifulSoup
#from requests.packages.urllib3.exceptions import InsecureRequestWarning

#This removes the urllib3 warnings 
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#####
# Edited malc0de's TotalHash script to work with the new TotalHash domain (https://totalhash.cymru.com)
# Instead of using URLLib, used Requests and Beautiful soup to do all of the work
# Enjoy!
#####

message = 'Python script search totalhash.com see http://totalhash.com/help/ for examples'
parser = OptionParser(message)
parser.add_option('-r', '--report', dest='r', help='print out analysis report ./totalhash.py -r sha256', action='store')
parser.add_option('-s', '--search', dest='s', help='search totalhash ./totalhash.py -s ip:127.0.0.1 (search terms: av: dnsrr: email: filename: hash: ip: mutex: pdb: registry: url: useragent: version: )', action='store')

(options, args) = parser.parse_args()

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)

if options.s:
    count = 0
    total = 0
    while count <= total:
        #Let's forge our User-agent string
        #TODO: Make this configurable as a parameter
        headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE+8.0; Windows NT 5.1; Trident/4.0;)'}
        #TODO: Add Trusted Root Certificate (GeoTrust) so I can remove the verify=False
        #Note: Remove verify=False if you want to ensure you're truly connecting with TotalHash. You'll need to add it's Root Certificate to your local trusted store
	if count == 0:
	        r = requests.get('https://totalhash.cymru.com/search/%s' % (options.s), headers=headers, verify=False)
	else:
	        r = requests.get('https://totalhash.cymru.com/search/%s/%s' % (options.s, count), headers=headers, verify=False)
        #TH is nice enough to put the number of results at the top of the page, so let's grab that and we can use that in our while loop
        results = re.findall("\x3ch3\x3eDisplaying.*?of (.*?) results\x3c\x2fh3\x3e", r.content, re.DOTALL)
        total = int(results[0])

        #If there is no results, exit
        if total == 0:
            break
        else:
            soup = BeautifulSoup(r.content, "html.parser")
            for table_ in soup.find_all('table'):
                trList = table_.find_all('tr')
                for tr in trList:
                    td = tr.find_all('td')
                    try:
                        #Set the sha1, timestamp and detection
                        sha1 = td[0].find('a').contents[0]
                        timestamp = td[1].contents[0]
                        detection = td[3].contents[0]
                        #If there is a detection, grab the contents of the <a> tag
                        if detection != 'N/A':
                            detectionText = detection.contents[0]
                        else:
                            detectionText = detection
                        #Print our results!
                        #TODO: Write this to a file and not stdout
                        print sha1 + "," + timestamp + "," + detectionText
                    except Exception, e:
                        #This occurs on the first row of the table (which is the header)
                        #TODO: Make this more elegant instead of in an exception. This could be bad
                        continue

	count = count + 20
