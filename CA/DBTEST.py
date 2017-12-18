from pymongo import MongoClient
import pprint,datetime

client=MongoClient()
db=client.pythondb
post = {"author": "Maxsu",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}
pp={"case":"2",
    "radius_1":[{
        "step_1":[
            {
                "time":0,
                "surplus":100
            },
            {
                "time":1,
                "surplus":99
            },
            {
                "time":10,
                "surplus":80
            }
        ],
        "step_2":[
            {
                "time":0,
                "surplus":100
            },
            {
                "time":1,
                "surplus":99
            },
            {
                "time":10,
                "surplus":80
            }
        ],
        "step_3":[
            {
                "time":0,
                "surplus":100
            },
            {
                "time":1,
                "surplus":99
            },
            {
                "time":10,
                "surplus":80
            }
        ]
    }],
    "radius_2":[{
        "step_1":[
            {
                "time":0,
                "surplus":100
            },
            {
                "time":1,
                "surplus":99
            },
            {
                "time":10,
                "surplus":80
            }
        ],
        "step_2":[
            {
                "time":0,
                "surplus":100
            },
            {
                "time":1,
                "surplus":99
            },
            {
                "time":10,
                "surplus":80
            }
        ],
        "step_3":[
            {
                "time":0,
                "surplus":100
            },
            {
                "time":1,
                "surplus":99
            },
            {
                "time":10,
                "surplus":80
            }
        ]
    }]
    }
posts=db.p2
post_id=posts.insert_one(pp).inserted_id
# print("pist id is ",post_id)
# cur=db.collection_names(include_system_collections=False)
# print(cur)
# posts=db.posts
# pprint.pprint(posts.find_one())