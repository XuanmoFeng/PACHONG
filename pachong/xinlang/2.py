#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
import re

out=open('code','wb')
def get_main(url1):
    page=urllib2.urlopen(url1);
    main_re=re.compile(".*<p>[^跟号吴没|^<aC](.*?)</p>");
    #(".*<div class=\"article article_16.*(?:.|[\r\n])*.+?<div class=\"article-info");
    #(".*<meta name=\"description\" content.*")#i.
    htm=main_re.findall(page.read());
    for j in htm:
        print j;
        out.write(j);
    print ;
    out.write('\n');
    out.write('\n');
        #j =unicode(j,"utf-8");
        #qq=re.compile("");
        #qq=re.compile("t=\"(.*?)/>")
        #lll=qq.findall(j);      #print lll;
        #for lin in lll:
            #lin=unicode(lin,"utf-8");
            #print lin;
            #print ;
            #print ;

url="http://news.sina.com.cn/world/"
request=urllib2.urlopen(url)
content =r"<li><a target.+?</a></li>"
da=re.compile(content)
ll= da.findall(request.read())
for line in ll:
    #line =unicode(line,"utf-8")
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
