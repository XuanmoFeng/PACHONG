#!/usr/bin/env python
# coding=utf-8
import urllib2
import urllib
def getCookieOpener():
    postUrl="http://www.douban.com/accounts/login"
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support)
    postData={
        "source":"index_nav",
        "redir":"http://www.douban.com/",
        "form_email":"18309220966",
        "form_password":"fengkai1314",
        "captcha-solution":"great",
        "captcha-id":"dc1HiARpI49wgtSML3f8RSnw:en",
        "login":"登陆"
    }
    postData = urllib.urlencode(postData)
    loginRequest = opener.open(postUrl,postData)
    return loginRequest.read();
