import random
import time

from flask import Flask, jsonify

import imitation_charger


app = Flask(__name__)


@app.route("/charger")
def index():
    return jsonify({'CHARGER': imitation_charger.charger_json()})


if __name__ == "__main__":
    app.run(debug=True)

