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
	
	def conut():
		return len(urlList)
	
	def geturlList():
		return urlList;
	
	def getLocalUrl():
		return self.url;
	
	def setLocalUrl(url):
		self.url=url;



head = EachPage("https://gcc.gnu.org/onlinedocs/");
	

def getpage(url):
	return urllib.urlopen(url).read();

def getallurlformpage(content):
	allurl=re.findall(r'.*?\"(https://.*?)\"',content.replace('\n','').replace('\t','').replace(' ',''),re.M|re.X|re.I);
	return  allurl
	#allurl[:]是 allurl 的一个内存拷贝
	
def getcurrenturl(url):
	url_temp=url;
	pattern=re.compile(r'^http.*\.(gz|pdf|ico|css)$');
	for i in url_temp[:]:
		if re.match(pattern,i.strip()):
			url_temp.remove(i)
	return url_temp
	
def Geturl(url):
	allpage=getpage(url);
	allurl=getallurlformpage(allpage);
	currenturl=getcurrenturl(allurl);
	return currenturl;

def RecursiveGetUrl(url):
	if not head.getLocalUrl():
		head.setLocalUrl(url);
	print head.getLocalUrl()
	url=Geturl(url);
	for i in url:
		print i
		if i:
			RecursiveGetUrl(i)
	

if __name__ == '__main__':
	RecursiveGetUrl("https://gcc.gnu.org/onlinedocs/")
	
