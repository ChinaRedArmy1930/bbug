#coding:utf-8
import urllib
import random 
import string
import re

class EachPage:
	urlList = [];

	def __init__(self,url):
		self.url = url
		pass
		
	def add(url):
		if url not in urlList:
			return urlList.append(url)
		else:
			return NULL;
	
	def addList(listurl):
		return urlList.extend(listurl);
	
	def conut(self):
		return len(urlList)
	
	def geturlList(self):
		return urlList;
	
	def getLocalUrl(self):
		return self.url;
	
	def setLocalUrl(url):
		self.url=url;



head = EachPage("https://gcc.gnu.org/onlinedocs/");
	

def getpage(url):
	fd = urllib.urlopen(url);
	if fd.getcode() == 200:
		return fd.read()
	else:
		print '\033[1m' + url + " requst failed!"+'\033[0m'
		return None
		
def getallurlformpage(content):
	if not content:
		return None;
	allurl=re.findall(r'.*?(href=\".*?\")',content.replace('\n','').replace('\t','').replace(' ',''),re.M|re.X|re.I);
	print allurl
	return  allurl
	
	
def getcurrenturl(url):
	if not url:
		return None;
	url_temp=url;
	pattern_del=re.compile(r'^href=.*\.(gz|pdf|ico|css)$');
	pattern_http=re.compile(r'^href=\"(http(s?):.*)[^(gz|pdf|ico|css)]\"');
	pattern_join=re.compile(r'^href=\"([^(http|mailto)]).*\"');
	#allurl[:]是 allurl 的一个内存拷贝
	for i in url_temp[:]:
		print i
		url_temp.remove(i)
		if re.match(pattern_del,i.strip()):
			print "del :"+i
			continue;
		if re.match(pattern_http,i.strip()):
			#去掉 herf:"  和 "
			url_temp.append(i[6:-1])
			continue;
		if re.match(pattern_join,i.strip()):
			print "join :"+i
			url_temp.append(temppage.getLocalUrl()+i[6:-1])
			continue;
	return url_temp
	
def Geturl(url):
	global temppage
	temppage = EachPage(url);
	allpage=getpage(url);
	allurl=getallurlformpage(allpage);
	currenturl=getcurrenturl(allurl);
	if not currenturl:
		return None
	for i in currenturl:
		#print i
		pass
	return currenturl;

def RecursiveGetUrl(url):
	if not head.getLocalUrl():
		head.setLocalUrl(url);
	print "==============================="
	print "headurl :"+url
	print "this page have this urls:"
	url=Geturl(url);
	if not url:
		return None
	for i in url:
		print i 
		if i:
			RecursiveGetUrl(i)
			pass
	

if __name__ == '__main__':
	RecursiveGetUrl("https://gcc.gnu.org/onlinedocs/gcc-8.2.0/gcc/Machine-Constraints.html#Machine-Constraints")
	
