import urllib
import urllib2

def post(url, data):
    head = {"Content-Type": "text/plain"}
    req = urllib2.Request(url,head)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data)
    return response.read()


def main():
    posturl = "http://10.199.169.218:8086/write?db=jmxdb"
    data = "topics1,all=0.00 trace=0.00\nplatform=1.50 app=0.00\napps_metrics=0.00 docker=9.20"
    print post(posturl, data)
if __name__ == '__main__':
    main()