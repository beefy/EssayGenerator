from urllib2 import Request, urlopen, URLError

request = Request('http://isbndb.com/api/books.xml?access_key=GGLY5SON&index1=title&value1=sea&results=details,texts')

try:
   response = urlopen(request)
   kittens = response.read()
   print kittens
except URLError, e:
   print 'No kittez. Got an error code:', e