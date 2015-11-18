import urllib3

url = 'http://www.acme.com/products/3322'
response = urllib3.get_host(url)
    #.urlopen(url).read()
print("The Response is  :",response)