#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
import re

out=open('code','wb')
urlfile=open('url','wb')
def get_main(url1):
    page=urllib2.urlopen(url1);
    main_re=re.compile(".*<p>[^跟号吴没<a|C](.*?)</p>");
    htm=main_re.findall(page.read());
    for j in htm:
        print j;
        out.write(j);
    print ;
    out.write('\n');
    out.write('\n');

url="http://news.sina.com.cn/world/"
request=urllib2.urlopen(url)
content =r"<li><a target.+?</a></li>"
da=re.compile(content)
ll= da.findall(request.read())
for line in ll:
    pp=re.compile("http://.+?ml")
    oo=re.compile(u"\">(.*?)<")
    m=pp.findall(line)
    p=oo.findall(line)
    for k in p:
        print k
        out.write(k);
        out.write('\n');
    for i in m:
        get_main(i)
        urlfile.write(i);
        urlfile.write('\n');
