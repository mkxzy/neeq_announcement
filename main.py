#!/usr/bin/env python

from urllib import request
import store
import jsonp as jp
import fetch_announcement as fa
from concurrent.futures import ThreadPoolExecutor as Pool
import time


def save_ann(c):
    companyCd = c['xxzqdm']
    ann_list = fa.fetch_all(companyCd)
    print("公司代码: %s" % companyCd)
    store.save_ann(ann_list)


pool = Pool(max_workers=20)
page = 0
while True:
    first_url = 'http://www.neeq.com.cn/nqxxController/nqxx.do?callback=ella&page=%s' % page
    print(first_url)
    res = request.urlopen(first_url)
    jsonp = res.read().decode('utf-8')
    json_obj = jp.parse_jsonp(jsonp)
    total_pages = json_obj[0]["totalPages"]
    cs = json_obj[0]['content']
    store.save_company(cs)
    results = pool.map(save_ann, cs)
    page = page + 1
    if page == total_pages:
        break
    time.sleep(0.02)
