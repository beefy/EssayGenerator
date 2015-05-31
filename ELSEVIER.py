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

#get doi_ids
doi_ids = []

while article.find('"prism:doi":"') != -1:
    cur_str = article[int(article.find('"prism:doi":"')):int(article.find('"prism:doi":"')+47)]
    cur_doi = cur_str[13:]
    #isOpenArticleStr = article[int(article.find('"openaccessArticle":')+20):int(article.find('"openaccessArticle":')+24)]
    #if isOpenArticleStr == 'true':
    doi_ids.append(cur_doi)
    article = article.replace(cur_str, ' ', 1)
    #article = article.replace(isOpenArticleStr, '  ')
    if len(doi_ids) >= 100:
        print doi_ids
        print 'Filled up!'
        exit(0)
print doi_ids


#get full article text
for i in range(0,len(doi_ids)):
    request = Request('http://api.elsevier.com/content/article/DIO:' + doi_ids[i] + '?APIKey=fc14ce8335d2899c36c25615b5feb68a&httpAccept=text/html')

    try:
        response = urlopen(request)
        article = response.read()
    except URLError, e:
        print 'Error, could not read file:', e

    #extract text in article (between <p> tags)
    while article.find("<p>") != -1:
        cur_text_bracket = article[int(article.find('<p>')):int(article.find('</p>') + 3)]
        cur_text = cur_text_bracket[3:len(cur_text_bracket)-4]

        article = article.replace(cur_text_bracket, ' ', 1)

        #nupic stuff
        print cur_text

print 'DONE'

