#coding:utf-8
import urllib
import re

def getpage(url):
	return urllib.urlopen(url)

def geturlformpage(content):
	pattern=re.compile(r'^http.*\.(gz|pdf|.ico)$');
	allurl=re.findall(r'.*?\"(https://.*?)\"',content,re.M|re.X|re.I);
	#allurl[:]是 allurl 的一个内存拷贝
	for i in allurl[:]:
		if re.match(pattern,i.strip()):
			allurl.remove(i)
	return allurl
if __name__ == '__main__':
	allpage=getpage("https://gcc.gnu.org/onlinedocs/").read();
	for i in geturlformpage(allpage.replace('\n','').replace('\t','').replace(' ','')):
		print i
	