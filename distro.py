#!/usr/bin/python

from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
import urllib2
from collections import OrderedDict
import re, json

title = []
imgUrl = []
price = []
links = []
linkdest = 'http://www.imperialdistro.com'
page = urllib2.urlopen(linkdest)
soup = BeautifulSoup(page)

halaman = soup.find('div', attrs={'class':'leftcategories'})
for link in halaman.findAll('a', href=True):
	i = link.get('href')
	x = linkdest + i
	links.append(x)

for b in links:
	page2 = urllib2.urlopen(b)
	soup2 = BeautifulSoup(page2)
	for image in soup2.findAll("td", {"class":"hotitems"}):
		for img in image.findAll("img"):
			
			imgUrl.append("http://www.imperialdistro.com"+img['src'])
			title.append(img['alt'])
		for hrg in image.findAll("span",{"class":"product-price"}):
			price.append(hrg.getText())

with open("imperial.html","a") as f:
	f.write("<html>\n")
	f.write("<body>\n")
	for i,j,k in zip(title,imgUrl, price):
		f.write("<h1>"+str(i)+"</h1>\n")
		f.write("<img src=\""+str(j)+"\""+"/>\n")
		f.write("<h3>"+str(k)+"</h3>\n")

hasiljson = json.dumps(zip(title,imgUrl,price))
with open("data.json", "w") as filejson:
	filejson.write(hasiljson)
