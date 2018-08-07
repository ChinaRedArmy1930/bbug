#coding:utf-8
import urllib
import re

def getpage(url):
	return urllib.urlopen(url).read();

def getallurlformpage(content):
	allurl=re.findall(r'.*?\"(https://.*?)\"',content.replace('\n','').replace('\t','').replace(' ',''),re.M|re.X|re.I);
	return  allurl
	#allurl[:]是 allurl 的一个内存拷贝
	
def getcurrenturl(url):
	url_temp=url;
	pattern=re.compile(r'^http.*\.(gz|pdf|.ico)$');
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
	url=Geturl(url);
	for i in url:
		print i
		if i:
			RecursiveGetUrl(url)
	
if __name__ == '__main__':
	RecursiveGetUrl("https://gcc.gnu.org/onlinedocs/")
	
