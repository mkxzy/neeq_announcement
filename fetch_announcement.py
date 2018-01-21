import urllib
from urllib import request
from urllib import parse
import jsonp


def fetch_all(company):
    ann_list = []
    page = 0
    while True:
        url = "http://www.neeq.com.cn/disclosureInfoController/infoResult.do?callback=ella&page=%s" % page
        form_data = { "disclosureType": "1", "companyCd": company}
        postdata = parse.urlencode(form_data)
        postdata = postdata.encode('utf-8')
        res = request.urlopen(url, postdata)
        content = res.read().decode('utf-8')
        json_obj = jsonp.parse_jsonp(content)
        page_data = json_obj[0]['listInfo']
        ann_list.extend(page_data['content'])
        page_total = page_data['totalPages']
        print("progress: %d/%d" % (page, page_total))
        page = page + 1
        if page >= page_total:
            print("遍历分页完成")
            break
    return ann_list


if __name__ == '__main__':
    data_all = fetch_all('430002')
    print(data_all)
