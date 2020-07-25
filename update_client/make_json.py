import random


def make_json(time):
    json_body = {
        "CHARGER":
        [
            {
                'name': 'charger1',
                'time': time,
                'used_latest': random.randint(100, 150),
                'stored_latest': random.randint(500, 600),
                "used_after_030": random.randint(100, 150),
                "used_after_060": random.randint(100, 150),
                "used_after_090": random.randint(100, 150),
                "used_after_120": random.randint(100, 150),
                "used_after_150": random.randint(100, 150),
                "used_after_180": random.randint(100, 150),
                "stored_after_030": random.randint(500, 600),
                "stored_after_060": random.randint(500, 600),
                "stored_after_090": random.randint(500, 600),
                "stored_after_120": random.randint(500, 600),
                "stored_after_150": random.randint(500, 600),
                "stored_after_180": random.randint(500, 600)
            },
            {
                'name': 'charger2',
                'time': time,
                'used_latest': random.randint(100, 150),
                'stored_latest': random.randint(500, 600),
                "used_after_030": random.randint(100, 150),
                "used_after_060": random.randint(100, 150),
                "used_after_090": random.randint(100, 150),
                "used_after_120": random.randint(100, 150),
                "used_after_150": random.randint(100, 150),
                "used_after_180": random.randint(100, 150),
                "stored_after_030": random.randint(500, 600),
                "stored_after_060": random.randint(500, 600),
                "stored_after_090": random.randint(500, 600),
                "stored_after_120": random.randint(500, 600),
                "stored_after_150": random.randint(500, 600),
                "stored_after_180": random.randint(500, 600)
            },
            {
                'name': 'charger3',
                'time': time,
                'used_latest': random.randint(100, 150),
                'stored_latest': random.randint(500, 600),
                "used_after_030": random.randint(100, 150),
                "used_after_060": random.randint(100, 150),
                "used_after_090": random.randint(100, 150),
                "used_after_120": random.randint(100, 150),
                "used_after_150": random.randint(100, 150),
                "used_after_180": random.randint(100, 150),
                "stored_after_030": random.randint(500, 600),
                "stored_after_060": random.randint(500, 600),
                "stored_after_090": random.randint(500, 600),
                "stored_after_120": random.randint(500, 600),
                "stored_after_150": random.randint(500, 600),
                "stored_after_180": random.randint(500, 600)
            },
            {
                'name': 'charger4',
                'time': time,
                'used_latest': random.randint(100, 150),
                'stored_latest': random.randint(500, 600),
                "used_after_030": random.randint(100, 150),
                "used_after_060": random.randint(100, 150),
                "used_after_090": random.randint(100, 150),
                "used_after_120": random.randint(100, 150),
                "used_after_150": random.randint(100, 150),
                "used_after_180": random.randint(100, 150),
                "stored_after_030": random.randint(500, 600),
                "stored_after_060": random.randint(500, 600),
                "stored_after_090": random.randint(500, 600),
                "stored_after_120": random.randint(500, 600),
                "stored_after_150": random.randint(500, 600),
                "stored_after_180": random.randint(500, 600)
            }
        ]
    }

    return json_body