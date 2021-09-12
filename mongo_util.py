import pymongo


class MongoUtil:

    def __init__(self):
        print("------starting to init Mongo connection---\n")
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client.test
        self.collection = self.db.expect

    def insert_one(self, data):
        self.collection.insert_one(data)

    def find_one(self, key):
        return self.collection.find_one({'req': key})

    def close(self):
        print("------close Mongo connection---\n")
        self.client.close()


if __name__ == "__main__":
    mogo = MongoUtil()
    result = mogo.find_one(key="123")
    if result is None:
        print("没有值")
    else:
        print(result)
