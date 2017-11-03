# ! /usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2,json,time,requests
from bs4 import BeautifulSoup
from influxdb import InfluxDBClient
url="http://10.190.50.113:22223/metrics"
def getJson(url):
    # 使用requests获取网页
    req = requests.get(url)
    html = req.text.encode('utf-8')
    # 使用BS提取内容
    soup = BeautifulSoup(html,"lxml")
    res = soup('p')[0].text
    res_json = json.loads(res)
    return res_json
def getMap(data):
    channelInfoMap={}
    #c_trace_info
    c_trace_ChannelSize = float(data['CHANNEL.c_trace']['ChannelSize'])
    c_trace_ChannelFillPercentage=float(data['CHANNEL.c_trace']['ChannelFillPercentage'])
    c_trace_EventTakeSuccessCount=int(data['CHANNEL.c_trace']['EventTakeSuccessCount'])
    c_trace_1_ChannelSize = float(data['CHANNEL.c_trace_1']['ChannelSize'])
    c_trace_1_ChannelFillPercentage = float(data['CHANNEL.c_trace_1']['ChannelFillPercentage'])
    c_trace_1_EventTakeSuccessCount = int(data['CHANNEL.c_trace_1']['EventTakeSuccessCount'])
    #c_nginx_info
    c_nginx_ChannelSize = float(data['CHANNEL.c_nginx']['ChannelSize'])
    c_nginx_ChannelFillPercentage=float(data['CHANNEL.c_nginx']['ChannelFillPercentage'])
    c_nginx_EventTakeSuccessCount = int(data['CHANNEL.c_nginx']['EventTakeSuccessCount'])
    c_nginx_1_ChannelSize = float(data['CHANNEL.c_nginx_1']['ChannelSize'])
    c_nginx_1_ChannelFillPercentage = float(data['CHANNEL.c_nginx_1']['ChannelFillPercentage'])
    c_nginx_1_EventTakeSuccessCount = int(data['CHANNEL.c_nginx_1']['EventTakeSuccessCount'])
    channelInfoMap["c_trace_ChannelSize"]=c_trace_ChannelSize
    channelInfoMap["c_trace_ChannelFillPercentage"] = c_trace_ChannelFillPercentage
    channelInfoMap["c_trace_EventTakeSuccessCount"] = c_trace_EventTakeSuccessCount
    channelInfoMap["c_trace_1_EventTakeSuccessCount"] = c_trace_1_EventTakeSuccessCount
    channelInfoMap["c_trace_1_ChannelSize"] = c_trace_1_ChannelSize
    channelInfoMap["c_trace_1_ChannelFillPercentage"] = c_trace_1_ChannelFillPercentage
    channelInfoMap["c_nginx_ChannelSize"] = c_nginx_ChannelSize
    channelInfoMap["c_nginx_ChannelFillPercentage"] = c_nginx_ChannelFillPercentage
    channelInfoMap["c_nginx_1_ChannelSize"] = c_nginx_1_ChannelSize
    channelInfoMap["c_nginx_1_ChannelFillPercentage"] = c_nginx_1_ChannelFillPercentage
    channelInfoMap["c_nginx_EventTakeSuccessCount"] = c_nginx_EventTakeSuccessCount
    channelInfoMap["c_nginx_1_EventTakeSuccessCount"] = c_nginx_1_EventTakeSuccessCount

    return channelInfoMap

client = InfluxDBClient('10.199.169.218', 8086, 'admin', 'admin', 'jmxdb')
while 1:
    data = getJson("http://10.190.50.113:22223/metrics")
    map = getMap(data)
    json_body = [
        {
            "measurement": "channel",
            "fields": map
        }
    ]
    client.write_points(json_body)
    time.sleep(5)

