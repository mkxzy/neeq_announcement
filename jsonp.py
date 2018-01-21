import json
import re


def parse_jsonp(jsonp):
    j = json.loads(re.findall(r'^\w+\((.*)\)$', jsonp)[0])
    return j
