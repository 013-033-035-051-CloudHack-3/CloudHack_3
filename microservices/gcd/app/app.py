from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_restful import Resource, Api
import math

app = Flask(__name__)
api = Api(app)

class GCD(Resource):
    def get(self, num1, num2):
        result = math.gcd(num1, num2)
        return {'result': result}

api.add_resource(GCD, '/<int(signed=True):num1>/<int(signed=True):num2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5055,
        host="0.0.0.0"
    )