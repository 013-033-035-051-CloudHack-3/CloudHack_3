from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_restful import Resource, Api
import math

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'
api = Api(app)

class LCM(Resource):
    def get(self, num1, num2):
        temp = math.gcd(num1, num2)
        result = (num1/temp) * num2
        return {'result': result}

api.add_resource(LCM, '/<int(signed=True):num1>/<int(signed=True):num2>')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5056,
        host="0.0.0.0"
    )