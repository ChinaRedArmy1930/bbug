#coding:utf-8
import urllib
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
	return urllib.urlopen(url).read();

def getallurlformpage(content):
	allurl=re.findall(r'.*?(href=\".*?\")',content.replace('\n','').replace('\t','').replace(' ',''),re.M|re.X|re.I);
	return  allurl
	#allurl[:]是 allurl 的一个内存拷贝
	
def getcurrenturl(url):
	url_temp=url;
	pattern_del=re.compile(r'*\.(gz|pdf|ico|css)$');
	pattern_http=re.compile(r'^href=\"(http:.*)\"');
	pattern_join=re.compile(r'^href=\"([^http])\"');
	#TODO 将HTTP开头的URL 和需要连接的URL 提取出来
	for i in url_temp[:]:
		if re.match(pattern_del,i.strip()):
			url_temp.remove(i)
	return url_temp
	
def Geturl(url):
	allpage=getpage(url);
	allurl=getallurlformpage(allpage);
	currenturl=getcurrenturl(allurl);
	for i in currenturl:
		print i
	return currenturl;

def RecursiveGetUrl(url):
	if not head.getLocalUrl():
		head.setLocalUrl(url);
	print "==============================="
	print "headurl :"+url
	print "this page have this urls:"
	url=Geturl(url);
	for i in url:
		print i 
		if i:
			RecursiveGetUrl(i)
	

if __name__ == '__main__':
	RecursiveGetUrl("https://gcc.gnu.org/onlinedocs/")
	
