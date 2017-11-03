import urllib2,json
from bs4 import BeautifulSoup
def getData(url):
    response = urllib2.urlopen(url)
    html=response.read()
    soup = BeautifulSoup(html,"lxml")
    tables=soup.findAll("table")
    topicSpd={}
    for tab in tables:
        tabAttrs=tab.attrs
        if "id" in tabAttrs.keys():
            if tabAttrs["id"]=="topics-table":
                trs=tab.tbody.findAll("tr")
                for tr in trs:
                    tds=tr.findAll("td")
                    topic=tds[0].a.text
                    speed=tds[-2].text
                    topicSpd[topic]=speed
                    # topicSpd.update(topic,speed)
    return topicSpd

# def post(url, data):
#     head = {"Content-Type": "text/plain"}
#     req = urllib2.Request(url,head)
#     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
#     response = opener.open(req, data)
#     return response.read()
#
# def getPostData(map,list):
#     i = 1
#     dataString="topics,"
#     for item in list:
#         dataString=dataString+item+"="+map[item]+" "
#         if i % 2 == 0:
#             dataString=dataString+"\n"
#         i=i+1
#     return dataString

map=getData("http://10.199.164.195:8090/clusters/platform/topics")
json=json.dumps(map)
print json
# topicList=["all","trace","platform","app","apps_metrics","docker"]
# dataString=getPostData(map,topicList)
# print dataString
# post("http://10.199.169.218:8086/write?db=jmxdb",dataString)
