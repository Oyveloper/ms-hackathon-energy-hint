import pymongo as pymongo


def connect_db():
    client = pymongo.MongoClient(
        "mongodb+srv://db_user:very_simple_password@cluster0.eu0ag.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    return client["han-data"]


def get_han_data() -> [(float, str)]:
    client = connect_db()

    return [(value['power'], value["timeStamp"].split("+")[0]) for value in client["datapoints"].find()]
