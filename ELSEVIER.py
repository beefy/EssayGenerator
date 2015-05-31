from urllib2 import Request, urlopen, URLError
from xml.dom import minidom
import xml.etree.ElementTree as ET
from lxml import etree

#querry for pii article number
#check for openaccessArticle
request = Request('http://api.elsevier.com/content/search/index:SCIDIR?APIKey=fc14ce8335d2899c36c25615b5feb68a&query=sea')


#load file
try:
    response = urlopen(request)
    article = response.read()
   
except URLError, e:
    print 'Error, could not read file:', e
    exit(1)

#get pip_ids
pii_ids = []

while article.find('pii:') != -1:
    cur_str = article[int(article.find('pii:')):int(article.find('pii:')+24)]
    cur_pii = cur_str[4:]
    #isOpenArticleStr = article[int(article.find('"openaccessArticle":')+20):int(article.find('"openaccessArticle":')+24)]
    #if isOpenArticleStr == 'true':
    pii_ids.append(cur_pii)
    article = article.replace(cur_str, ' ', 1)
    #article = article.replace(isOpenArticleStr, '  ')
    if len(pii_ids) >= 100:
        print pii_ids
        print 'Filled up!'
        exit(0)
print pii_ids

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

