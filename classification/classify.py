#!/bin/bash python
#encoding=utf8

import sys
#import urllib.request 
#import urllib.parse
import json

url = "http://192.168.200.73:5555/golaxyNlpClassification/golaxy/nlp/classification/chinese/news/golaxyPublicOpinion/v1"
headers = {'Content-Type': 'application/json'}

f = open(sys.argv[1],'r')
s = f.readlines()
f.close()

import urllib
import urllib2
    
for line in s:
	postdata = []
	postdata.append(line)
	data = json.dumps(postdata)
	req = urllib2.Request(url=url,headers=headers, data=data)
	response = urllib2.urlopen(req)
	out = response.read()
#	print out 
	jd = json.loads(out)
	scy = jd["classificationResults"]
	sentiscore = scy[0]["label"]
	firstclass = sentiscore.split("/")[0]
	print firstclass	

"""
def build_data(line):
	postdata = []
	postdata.append(line)
	data = json.dumps(postdata)
	return data

def send_data(url,data):
	req = urllib.request.urlopen(url, data)
	out = req.read()
	print(out)

for line in s:
	postdata = 
	data = build_data(line)
	send_data(url,data)
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '[""]' 'http://192.168.200.75:19006/golaxy/nlp/classification/chinese/news/golaxyPublicOpinion/v1'  
"""
