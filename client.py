import pymongo

def get_database():
    from pymongo import MongoClient
    import pymongo

  
    CONNECTION_STRING = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/umuziclients"

  
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

  
    return client['user_shopping_list']

if __name__ == "__main__":    

    dbname = get_database()