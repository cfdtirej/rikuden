
import time
import random


def charger_json():
    current_time = int(time.time())
    json_body = [
        {
            'name': 'charger1',
            'time': current_time,
            'used_latest': random.randint(100, 150),
            'stored_latest': random.randint(500, 600),
            "used_after_30min": random.randint(100, 150),
            "used_after_60min": random.randint(100, 150),
            "used_after_90min": random.randint(100, 150),
            "used_after_120min": random.randint(100, 150),
            "used_after_150min": random.randint(100, 150),
            "used_after_180min": random.randint(100, 150),
            "stored_after_30min": random.randint(500, 600),
            "stored_after_60min": random.randint(500, 600),
            "stored_after_90min": random.randint(500, 600),
            "stored_after_120min": random.randint(500, 600),
            "stored_after_150min": random.randint(500, 600),
            "stored_after_180min": random.randint(500, 600)
        },
        {
            'name': 'charger2',
            'time': current_time,
            'used_latest': random.randint(100, 150),
            'stored_latest': random.randint(500, 600),
            "used_after_30min": random.randint(100, 150),
            "used_after_60min": random.randint(100, 150),
            "used_after_90min": random.randint(100, 150),
            "used_after_120min": random.randint(100, 150),
            "used_after_150min": random.randint(100, 150),
            "used_after_180min": random.randint(100, 150),
            "stored_after_30min": random.randint(500, 600),
            "stored_after_60min": random.randint(500, 600),
            "stored_after_90min": random.randint(500, 600),
            "stored_after_120min": random.randint(500, 600),
            "stored_after_150min": random.randint(500, 600),
            "stored_after_180min": random.randint(500, 600)
        },
        {
            'name': 'charger3',
            'time': current_time,
            'used_latest': random.randint(100, 150),
            'stored_latest': random.randint(500, 600),
            "used_after_30min": random.randint(100, 150),
            "used_after_60min": random.randint(100, 150),
            "used_after_90min": random.randint(100, 150),
            "used_after_120min": random.randint(100, 150),
            "used_after_150min": random.randint(100, 150),
            "used_after_180min": random.randint(100, 150),
            "stored_after_30min": random.randint(500, 600),
            "stored_after_60min": random.randint(500, 600),
            "stored_after_90min": random.randint(500, 600),
            "stored_after_120min": random.randint(500, 600),
            "stored_after_150min": random.randint(500, 600),
            "stored_after_180min": random.randint(500, 600)
        },
        {
            'name': 'charger4',
            'time': current_time,
            'used_latest': random.randint(100, 150),
            'stored_latest': random.randint(500, 600),
            "used_after_30min": random.randint(100, 150),
            "used_after_60min": random.randint(100, 150),
            "used_after_90min": random.randint(100, 150),
            "used_after_120min": random.randint(100, 150),
            "used_after_150min": random.randint(100, 150),
            "used_after_180min": random.randint(100, 150),
            "stored_after_30min": random.randint(500, 600),
            "stored_after_60min": random.randint(500, 600),
            "stored_after_90min": random.randint(500, 600),
            "stored_after_120min": random.randint(500, 600),
            "stored_after_150min": random.randint(500, 600),
            "stored_after_180min": random.randint(500, 600)
        }
    ]
    return json_body
