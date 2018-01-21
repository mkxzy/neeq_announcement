from pymongo import MongoClient


client = MongoClient('127.0.0.1', 27017)
db = client.neeq


def save_company(cs):
    result = db.company.insert_many(cs)
    return result

def save_ann(ann_list):
    return db.announce.insert_many(ann_list)

if __name__ == '__main__':
    cs = [{"a:": "b"}]
    save_company(cs)
