import pymongo

client = pymongo.MongoClient()

db = client.movies

coll = db.movies

#part A
upresult = coll.update_many(
    {"rated":"NOT RATED"},
    {
        "$set":{"rated":"Pending rating"}, 
        "$currentDate":{"lastModified":True}
    }
)

#part B

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
)


#part C
cursor = coll.aggregate(
    [
        {"$unwind":"$genre"},
        {"$match":{"genre":"Documentary"}},
        {"$group":{"_id":"Documentary","count":{"$sum":1}}}
    ]
)

print cursor

#part D
cursor1 = coll.aggregate(
    [
        {"$unwind":"$countries"},
        {"$match":{"rated":"Pending rating","countries":"USA"}},
        {"$group":{"_id":{"country":"USA","rating":"Pending rating"},"count":{"$sum":1}}}
    ]
)

print cursor1
