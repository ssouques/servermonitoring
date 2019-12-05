import logging
import logging.config

import json

from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_jwt_extended import JWTManager

from servermonitoring.api import Monitors

#logging.config.fileConfig('config/logging.monitoring.conf')

logging.info("############################################################")
logging.info("#                                                          #")
logging.info("#                STARTING MONITORING SERVER                #")
logging.info("#                                                          #")
logging.info("############################################################")

app = Flask(__name__)


def startserver(port=None, endpoint='/api/monitoring/status'):
    api = Api(app)
    api.add_resource(Monitors, endpoint)
    app.run(debug=False, port=port)

if __name__ == "__main__":
    startserver()
