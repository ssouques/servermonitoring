from flask import jsonify, send_file
from flask_restful import Resource, request

import psutil

class Monitors(Resource):

    def get(self):
        return {
            'cpu_usage':psutil.cpu_percent(interval=None),  
            'memory_usage':psutil.virtual_memory().percent,
            'memory_available':psutil.virtual_memory().available,
        }
