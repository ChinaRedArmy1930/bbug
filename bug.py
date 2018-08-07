#coding:utf-8
import urllib
import re

def getpage(url):
	return urllib.urlopen(url)
#href=\"https:.*\"
def geturlformpage(content):
	pattern=re.compile(r'^http.*\.(gz|pdf)$');
	allurl=re.findall(r'.*?\"(https://.*?)\"',content,re.M|re.X|re.I);
	for i in allurl:
		pass
		print i
	for i in allurl:
		if re.match(pattern,i.strip()):
			#print i
			allurl.remove(i)
	print len(allurl)
	for i in allurl:
		pass	
		print i
	return allurl
if __name__ == '__main__':
	allpage=getpage("https://gcc.gnu.org/onlinedocs/").read();
	geturlformpage(allpage.replace('\n','').replace('\t','').replace(' ',''))
	