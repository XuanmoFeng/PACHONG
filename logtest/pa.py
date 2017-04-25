#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2

def getCookieOpener():
    postUrl="http://qzone.qq.com"
    filename='cookie.txt'
    cj = cookielib.MozillaCookieJar(filename)
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support)
    postData={
        "app":"adv",
        "return":"http://user.qzone.qq.com/",
        "username":"763608087",
        "password":"asdzxc123789"

    }

    postData = urllib.urlencode(postData)
    loginRequest = opener.open(postUrl,postData)
    print loginRequest.read()
    return opener
