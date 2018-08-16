#coding:utf-8
import urllib
import random 
import string
import re
import requests

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


UrlSet = set()
head = EachPage("https://gcc.gnu.org/onlinedocs/");
deeplength=0

def getpage(url):
	header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'};# chrome header
	req = requests.get(url,headers=header,verify=False);
	if req.status_code == 200:
		return req.text
	else:
		print '\033[1m' + url +','+str(fd.getcode())+','+'requst failed!'+'\033[0m'
		return None

		
def getallurlformpage(content):
	if not content:
		return None;
	allurl=re.findall(r'.*?(href=\".*?\")',content.replace('\n','').replace('\t','').replace(' ',''),re.M|re.X|re.I);
	#print allurl
	return  allurl
	
	
def getcurrenturl(url):
	if not url:
		return None;
	url_temp=url;
	pattern_del=re.compile(r'^(href=)\".*\.(gz|pdf|ico|css)\"$');
	pattern_http=re.compile(r'^(href=)\"http(s?):.*?(?!(gz|pdf|ico|css))\"');
	pattern_join=re.compile(r'^(href=)\"(?!(http|mailto)).*?(?!(gz|pdf|ico|css))\"');
	#allurl[:]是 allurl 的一个内存拷贝
	for i in url_temp[:]:
		#print i
		url_temp.remove(i)
		if re.match(pattern_del,i.strip()):
			#print "del :"+i
			continue;
		if re.match(pattern_http,i.strip()):
			#去掉 herf:"  和 "
			#print "http :"+i
			if i[6:-1] not in url_temp:
				url_temp.append(i[6:-1])
				UrlSet.add(i[6:-1])
			continue;
		if re.match(pattern_join,i.strip()):
			#print "join :"+i
			if temppage.getLocalUrl()+i[6:-1] not in url_temp:
				url_temp.append(temppage.getLocalUrl()+i[6:-1])
				UrlSet.add(temppage.getLocalUrl()+i[6:-1])
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

def RecursiveGetUrl(url,number):
	UrlSet.add(url)
	print "number of UrlSet = %d"%len(UrlSet)
	if len(UrlSet) > number:
		return;
	url=Geturl(url);
	if not url:
		return None
	for i in url:
		#print i 
		if i:
			RecursiveGetUrl(i,number)
			pass
	

if __name__ == '__main__':
	#递归遍历起始url找500个页面
	RecursiveGetUrl("https://gcc.gnu.org/onlinedocs/gcc-8.2.0/gcc/DEC-Alpha-Options.html#DEC-Alpha-Options",500)
	with open('url.txt','w') as urlFile:
		for i in UrlSet:
			urlFile.writelines(i+"\n");
		
