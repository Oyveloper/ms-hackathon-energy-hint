import pymongo as pymongo


def connect_db():
    client = pymongo.MongoClient(
        "mongodb+srv://db_user:very_simple_password@cluster0.eu0ag.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    return client["han-data"]


def get_han_data():
    client = connect_db()

    return [value['power'] for value in client["datapoints"].find()]
