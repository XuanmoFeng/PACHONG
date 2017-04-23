#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2

values={}
values['form_email']="18309220966"
values['form_password']="fengkai1314"
data=urllib.urlencode(values)
url="https://www.douban.com/accounts/login"
request = urllib2.Request(url,data)
response=urllib2.urlopen(request)
print response.read()


