# import json
import pprint
import requests
import time
import random

import charger_graph
import settings


def main(charger_json):
    charger = charger_graph.ChargerGraph(settings.HOST, settings.AUTH, **charger_json)
    charger.update_charger_graph()
    return None


if __name__ == '__main__':
    # api_request = requests.get(settings.API_URL)
    current_time = int(time.time())

    charger1_json = settings.graph_json
    charger1_json['Label'] = 'Charger1'
    charger1_json['north'] = settings.charger1['relation']['north']
    charger1_json['south'] = settings.charger1['relation']['south']
    charger1_json['west'] = settings.charger1['relation']['west']
    charger1_json['east'] = settings.charger1['relation']['east']
    charger1_json['name'] = 'charger1'
    charger1_json['meshcode'] = settings.charger1['meshcode']
    charger1_json['latitude'] = settings.charger1['latitude']
    charger1_json['longitude'] = settings.charger1['longitude']
    charger1_json['time'] = current_time
    charger1_json['used_latest'] = random.randint(100, 150)
    charger1_json['stored_latest'] = random.randint(500, 600)
    charger1_json['used_after_030'] = random.randint(100, 150)
    charger1_json['used_after_060'] = random.randint(100, 150)
    charger1_json['used_after_090'] = random.randint(100, 150)
    charger1_json['used_after_120'] = random.randint(100, 150)
    charger1_json['used_after_150'] = random.randint(100, 150)
    charger1_json['used_after_180'] = random.randint(100, 150)
    charger1_json['stored_after_030'] = random.randint(500, 600)
    charger1_json['stored_after_060'] = random.randint(500, 600)
    charger1_json['stored_after_090'] = random.randint(500, 600)
    charger1_json['stored_after_120'] = random.randint(500, 600)
    charger1_json['stored_after_150'] = random.randint(500, 600)
    charger1_json['stored_after_180'] = random.randint(500, 600)
    main(charger1_json)

    charger2_json = settings.graph_json
    charger2_json['Label'] = 'Charger2'
    charger2_json['north'] = settings.charger2['relation']['north']
    charger2_json['south'] = settings.charger2['relation']['south']
    charger2_json['west'] = settings.charger2['relation']['west']
    charger2_json['east'] = settings.charger2['relation']['east']
    charger2_json['name'] = 'charger2'
    charger2_json['meshcode'] = settings.charger2['meshcode']
    charger2_json['latitude'] = settings.charger2['latitude']
    charger2_json['longitude'] = settings.charger2['longitude']
    charger2_json['time'] = current_time
    charger2_json['used_latest'] = random.randint(100, 150)
    charger2_json['stored_latest'] = random.randint(500, 600)
    charger2_json['used_after_030'] = random.randint(100, 150)
    charger2_json['used_after_060'] = random.randint(100, 150)
    charger2_json['used_after_090'] = random.randint(100, 150)
    charger2_json['used_after_120'] = random.randint(100, 150)
    charger2_json['used_after_150'] = random.randint(100, 150)
    charger2_json['used_after_180'] = random.randint(100, 150)
    charger2_json['stored_after_030'] = random.randint(500, 600)
    charger2_json['stored_after_060'] = random.randint(500, 600)
    charger2_json['stored_after_090'] = random.randint(500, 600)
    charger2_json['stored_after_120'] = random.randint(500, 600)
    charger2_json['stored_after_150'] = random.randint(500, 600)
    charger2_json['stored_after_180'] = random.randint(500, 600)
    main(charger2_json)

    charger3_json = settings.graph_json
    charger3_json['Label'] = 'Charger3'
    charger3_json['north'] = settings.charger3['relation']['north']
    charger3_json['south'] = settings.charger3['relation']['south']
    charger3_json['west'] = settings.charger3['relation']['west']
    charger3_json['east'] = settings.charger3['relation']['east']
    charger3_json['name'] = 'charger3'
    charger3_json['meshcode'] = settings.charger3['meshcode']
    charger3_json['latitude'] = settings.charger3['latitude']
    charger3_json['longitude'] = settings.charger3['longitude']
    charger3_json['time'] = current_time
    charger3_json['used_latest'] = random.randint(100, 150)
    charger3_json['stored_latest'] = random.randint(500, 600)
    charger3_json['used_after_030'] = random.randint(100, 150)
    charger3_json['used_after_060'] = random.randint(100, 150)
    charger3_json['used_after_090'] = random.randint(100, 150)
    charger3_json['used_after_120'] = random.randint(100, 150)
    charger3_json['used_after_150'] = random.randint(100, 150)
    charger3_json['used_after_180'] = random.randint(100, 150)
    charger3_json['stored_after_030'] = random.randint(500, 600)
    charger3_json['stored_after_060'] = random.randint(500, 600)
    charger3_json['stored_after_090'] = random.randint(500, 600)
    charger3_json['stored_after_120'] = random.randint(500, 600)
    charger3_json['stored_after_150'] = random.randint(500, 600)
    charger3_json['stored_after_180'] = random.randint(500, 600)
    main(charger3_json)

    charger4_json = settings.graph_json
    charger4_json['Label'] = 'Charger4'
    charger4_json['north'] = settings.charger4['relation']['north']
    charger4_json['south'] = settings.charger4['relation']['south']
    charger4_json['west'] = settings.charger4['relation']['west']
    charger4_json['east'] = settings.charger4['relation']['east']
    charger4_json['name'] = 'charger4'
    charger4_json['meshcode'] = settings.charger4['meshcode']
    charger4_json['latitude'] = settings.charger4['latitude']
    charger4_json['longitude'] = settings.charger4['longitude']
    charger4_json['time'] = current_time
    charger4_json['used_latest'] = random.randint(100, 150)
    charger4_json['stored_latest'] = random.randint(500, 600)
    charger4_json['used_after_030'] = random.randint(100, 150)
    charger4_json['used_after_060'] = random.randint(100, 150)
    charger4_json['used_after_090'] = random.randint(100, 150)
    charger4_json['used_after_120'] = random.randint(100, 150)
    charger4_json['used_after_150'] = random.randint(100, 150)
    charger4_json['used_after_180'] = random.randint(100, 150)
    charger4_json['stored_after_030'] = random.randint(500, 600)
    charger4_json['stored_after_060'] = random.randint(500, 600)
    charger4_json['stored_after_090'] = random.randint(500, 600)
    charger4_json['stored_after_120'] = random.randint(500, 600)
    charger4_json['stored_after_150'] = random.randint(500, 600)
    charger4_json['stored_after_180'] = random.randint(500, 600)
    main(charger4_json)


