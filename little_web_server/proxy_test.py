import urllib2


def get_url():
    url = 'http://www.baidu.com'
    proxy = 'http://1.34.63.17:80'
    proxy_handle = urllib2.ProxyHandler({'http': proxy})
    opener = urllib2.build_opener(proxy_handle)
    response = opener.open(url)
    print response

get_url()