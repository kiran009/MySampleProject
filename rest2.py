#! /usr/bin/python2.7
import urllib2

url = 'http://www.acme.com/products/3322'
response = urllib2.urlopen(url,data=None)
    #.urlopen(url).read()
print("The Response is  :",response)