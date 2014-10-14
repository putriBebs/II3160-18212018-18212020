#II3160-18212018-18212020
#========================

#!/usr/bin/python

from xml.dom import minidom
import urllib
url='http://www.antaranews.com/rss/terkini'
xmldoc = minidom.parse(urllib.urlopen(url))
itemlist = xmldoc.getElementsByTagName('item')
print len(itemlist)
for s in itemlist:
	with open("foo.txt", "r+") as f:
		old = f.read() # read everything in the file
		f.seek(0) # rewind
		f.write(s.childNodes[5].childNodes[0].nodeValue + "\n" + s.childNodes[1].childNodes[0].nodeValue + "\n" + s.childNodes[3].childNodes[0].nodeValue + "\n" + old)
