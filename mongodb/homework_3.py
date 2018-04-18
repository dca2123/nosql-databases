import pymongo

client = pymongo.MongoClient()

db = client.movies

coll = db.movies

upresult = coll.update_many(
    {"rated":"NOT RATED"},
    {
        "$set":{"rated":"Pending rating"}, 
        "$currentDate":{"lastModified":True}
    }
)
'''
insert_result = coll.insert_one(
    {
        "title":"13th",
        "year":2016,
        "countries":["USA"],
        "genres":["Documentary","Crime","History"],
        "directors":["Ava DuVernay"],
        "imdb":{
            "id":789,
            "rating":8.2,
            "votes":16532
        }
    }
'''



