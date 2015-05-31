from urllib2 import Request, urlopen, URLError
from xml.dom import minidom

#querry for pii article number
#check for openaccessArticle
request = Request('http://api.elsevier.com/content/search/index:SCIDIR?APIKey=fc14ce8335d2899c36c25615b5feb68a&query=sea&API')

try:
   response = urlopen(request)
   article = response.read()
   #print article
   xmldoc = minidom.parse(article)
   itemlist = xmldoc.getElementsByTagName('pii')
   #print(len(itemlist))
except URLError, e:
   print 'Error, could not read file:', e

#for i in range(0,article.totalResults):
   #print i

#get full article text
#process data within <p> tags
request = Request('http://api.elsevier.com/content/article/PII:S0967-0637(15)00069-2?APIKey=fc14ce8335d2899c36c25615b5feb68a&httpAccept=text/html')

try:
   response = urlopen(request)
   article = response.read()
   #print article
except URLError, e:
   print 'Error, could not read file:', e

print 'DONE'

