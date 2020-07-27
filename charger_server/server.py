import json
import socketserver

import charger_graph
import settings



def update_charger_node(charger_json):
    charger = charger_graph.ChargerGraph(settings.HOST, settings.AUTH, **charger_json)
    charger.update_charger_graph()
    return None


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(4096).strip()
        j = json.loads(self.data.decode())
        c1_json = j["CHARGER"][0]
        c1_json.update(settings.c1_info)
        update_charger_node(c1_json)
        print('update ' + str(c1_json['name']))

        c2_json = j["CHARGER"][1]
        c2_json.update(settings.c2_info)
        update_charger_node(c2_json)
        print('update ' + str(c2_json['name']))

        c3_json = j["CHARGER"][2]
        c3_json.update(settings.c3_info)
        update_charger_node(c3_json)
        print('update ' + str(c3_json['name']))

        c4_json = j["CHARGER"][3]
        c4_json.update(settings.c4_info)
        update_charger_node(c4_json)
        print('update ' + str(c4_json['name']))
        print('--------Done:'+str(c4_json['time'])+'-----------')

        self.request.sendall(b'collect')


if __name__ == "__main__":
    server_HOST = 'localhost'
    server_PORT = 50002

    while True:
        with socketserver.TCPServer((server_HOST, server_PORT), MyTCPHandler) as server:
            server.serve_forever()