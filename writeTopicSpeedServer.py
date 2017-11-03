import urllib2,json,time
from bs4 import BeautifulSoup
from influxdb import InfluxDBClient
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
                    speed=float(speed)
                    topicSpd[topic]=speed
    return topicSpd

def getJson(url):
    response = urllib2.urlopen(url)
    html=response.read()
    soup = BeautifulSoup(html,"lxml")
    metrics=soup.findAll("p")
    return  metrics[0]

client = InfluxDBClient('10.199.169.218', 8086, 'admin', 'admin', 'jmxdb')
while 1:
    # data = getData("http://10.190.50.113:8090/clusters/platform/topics")
    data = getJson("http://10.190.50.113:22223/metrics")
    print data
    # json_body = [
    #     {
    #         "measurement": "topics",
    #         "fields": data
    #     }
    # ]
    # client.write_points(json_body)
    time.sleep(5)



