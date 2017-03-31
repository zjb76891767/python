#!/usr/bin/env python
# -*- coding: utf-8 -*-
# version python27
'''
批量检查url返回状态码
'''
import requests,sys,time
keyfile = 'url.txt'
try:
    keyhd=open(keyfile,'rb')
except:
    sys.stdout.write("Can not open %s\n"%keyfile)
    sys.exit()
while True:
    key = keyhd.readline()
    key=key.strip().lstrip("\xef\xbb\xbf")
    url = "http://%s"%key
    if not key:break
    if len(key) == 0: continue
    try:
        code=requests.get(url).status_code
        print key+'  %d'%code
    except:
        print key+'  none'
    time.sleep(1)
    sys.stdout.flush()
        
sys.exit(0)
