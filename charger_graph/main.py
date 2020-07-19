# import json
import pprint
import requests

import charger_graph
import settings


def main(charger_json):
    charger = charger_graph.ChargerGraph(settings.HOST, settings.AUTH, **charger_json)
    is_graph = charger.is_charger_graph()

    if is_graph == None:
        charger.merge_charger_graph()

    charger.update_charger_graph()

    return None


if __name__ == '__main__':
    api_request = requests.get(settings.API_URL)

    charger1_json = api_request.json()["CHARGER"][0]
    charger1_json.update(settings.charger1_json)
    main(charger1_json)

    charger2_json = api_request.json()["CHARGER"][1]
    charger2_json.update(settings.charger2_json)
    main(charger2_json)

    charger3_json = api_request.json()["CHARGER"][2]
    charger3_json.update(settings.charger3_json)
    main(charger3_json)

    charger4_json = api_request.json()["CHARGER"][3]
    charger4_json.update(settings.charger4_json)
    main(charger4_json)
