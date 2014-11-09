import urllib2

def getIP():
    pub_ip = urllib2.urlopen('http://ip.42.pl/raw').read()
    return pub_ip
