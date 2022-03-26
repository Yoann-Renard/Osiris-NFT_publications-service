from bson import ObjectId
from datetime import datetime

publication_example = {
    "_id": "5bf142459b72e12b2b1b2cd",
    "publication_date": "1999-12-31 23:59:59.999999",
    "user_name": "foo",
    "content_type": "image",
    "media_url": "https://image.com/img.png",
    "category": "photography",
    "description": "this is the description",
    "hashtags": ["hashtag1", "hashtag2", "hashtag3"],
    "likes_count": 23,
    "comments": [
        {
            "_id": "5bf142459b72e12b2b1b2ce",
            "user": "bar",
            "plublication_date": "2000-12-31 23: 59: 59.999469",
            "content": "comment example",
            "likes_count": 10,
            "replies": [
                {
                    "_id": "5bf142459b72e12b2b1b2c3",
                    "user": "foo",
                    "plublication_date": "2001-11-30 20: 10: 42.442765",
                    "target_user": "bar",
                    "content": "reply example",
                    "likes_count": 2
                }
            ]
        }
    ]
}

comment_example = {
    "_id": "5bf142459b72e12b2b1b2cd",
    "user": "foo",
    "publication_date": "1999-12-31 23:59:59.999999",
    "content": "comment example",
    "likes_count": 0,
    "replies": []
}

reply_example = {
    "_id": "5bf142459b72e12b2b1b2cd",
    "user": "foo",
    "target_user": "bar",
    "publication_date": "1999-12-31 23:59:59.999999",
    "content": "reply example",
    "likes_count": 0,
}

samples = [
    {
        "_id": ObjectId(),
        "publication_date": str(datetime.now()),
        "publication_name": "Chat Qui Fly",
        "user_name": "AutrePersonne",
        "content_type": "image",
        "media_url": "https://http.cat/100",
        "category": "photography",
        "description": "this is just a cat :))",
        "hashtags": ["#cat", "#cute", "#theywillkillyou"],
        "likes_count": 23,
        "comments":[
            {
                "_id": ObjectId(),
                "user": "mamamiaDu93",
                "plublication_date": str(datetime.now()),
                "content": "to cute for me i'm dying xO",
                "likes_count": 10,
                "replies": [
                    {
                        "_id": ObjectId(),
                        "user": "notsusatall",
                        "plublication_date": str(datetime.now()),
                        "target_user": "mamamiaDu93",
                        "content": "Right bro :3",
                        "likes_count": 2
                    }
                ]
            },
            {
                "_id": ObjectId(),
                "user": "LostOnTweeter",
                "plublication_date": str(datetime.now()),
                "content": "ratio.",
                "likes_count": 327,
                "replies": []
            }
        ]
    },
    {
        "_id": ObjectId(),
        "publication_date": str(datetime.now()),
        "publication_name": "Let Me In",
        "user_name": "EliseLaBalise",
        "content_type": "image",
        "media_url": "https://http.cat/401",
        "category": "photography",
        "description": "bruh wth my cat doin",
        "hashtags": ["#cat", "#401", "#solost"],
        "likes_count": 203,
        "comments":[
            {
                "_id": ObjectId(),
                "user": "jokesterdu13",
                "plublication_date": str(datetime.now()),
                "content": "where the cat lol",
                "likes_count": 10,
                "replies": [
                    {
                        "_id": ObjectId(),
                        "user": "Ayaya",
                        "plublication_date": str(datetime.now()),
                        "target_user": "jokesterdu13",
                        "content": "ahah",
                        "likes_count": 5
                    },
                    {
                        "_id": ObjectId(),
                        "user": "ImBored",
                        "plublication_date": str(datetime.now()),
                        "target_user": "Ayaya",
                        "content": "Not impressed, maybe you meant 'haha' ?",
                        "likes_count": 0
                    }
                ]
            }
        ]
    },
    {
        "_id": ObjectId(),
        "publication_date": str(datetime.now()),
        "publication_name": "Good Meal",
        "user_name": "EliseLaBalise",
        "content_type": "image",
        "media_url": "https://http.cat/405",
        "category": "photography",
        "description": "Poor cat vs hungry man",
        "hashtags": ["#poor", "#steak"],
        "likes_count": 195,
        "comments":[
            {
                "_id": ObjectId(),
                "user": "NotMyBusiness",
                "plublication_date": str(datetime.now()),
                "content": "Noooooooooo",
                "likes_count": 10,
                "replies": [
                    {
                        "_id": ObjectId(),
                        "user": "Joykiller",
                        "plublication_date": str(datetime.now()),
                        "target_user": "NotMyBusiness",
                        "content": "RUNNN",
                        "likes_count": 4
                    }
                ]
            },
            {
                "_id": ObjectId(),
                "user": "MathieuDeToulon",
                "plublication_date": str(datetime.now()),
                "content": "Le J c'est le S.",
                "likes_count": 27,
                "replies": [
                    {
                        "_id": ObjectId(),
                        "user": "ChocolatineMaster",
                        "plublication_date": str(datetime.now()),
                        "target_user": "MathieuDeToulon",
                        "content": "ahaha",
                        "likes_count": 5
                    },
                    {
                        "_id": ObjectId(),
                        "user": "Ayaya",
                        "plublication_date": str(datetime.now()),
                        "target_user": "MathieuDeToulon",
                        "content": "C paris bb",
                        "likes_count": 1
                    }
                ]
            }
        ]
    },
    {
        "_id": ObjectId(),
        "publication_date": str(datetime.now()),
        "publication_name": "Chat Qui Fly moyen",
        "user_name": "AutrePersonne",
        "content_type": "image",
        "media_url": "https://http.cat/404",
        "category": "photography",
        "description": "it is a cat yesss :))",
        "hashtags": ["#cat", "#theywillkillyou"],
        "likes_count": 4444,
        "comments":[
            {
                "_id": ObjectId(),
                "user": "yokaaa",
                "plublication_date": str(datetime.now()),
                "content": "giga chad cat",
                "likes_count": 100,
                "replies": [
                    {
                        "_id": ObjectId(),
                        "user": "poopoDu13",
                        "plublication_date": str(datetime.now()),
                        "target_user": "yokaaa",
                        "content": "Right man",
                        "likes_count": 22
                    }
                ]
            },
            {
                "_id": ObjectId(),
                "user": "kakak",
                "plublication_date": str(datetime.now()),
                "content": "ratio.",
                "likes_count": 327,
                "replies": []
            }
        ]
    }
]
