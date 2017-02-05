#coding=utf-8
import re
import urllib2
import urllib

html = urllib.urlopen("http://tieba.baidu.com/p/4180696186")
html_read = html.read()
re_rule = r'src="(.+?\.jpg)" size='
re_complie = re.compile(re_rule)
re_findall = re.findall(re_complie,html_read)
print re_findall
x = 0

for getimg in re_findall: #可能会将列表[]初始化为非列表,要不会报错
    print 'download: %s ....done' % (x);urllib.urlretrieve(getimg,"%s.jpg" % x);x+=1
