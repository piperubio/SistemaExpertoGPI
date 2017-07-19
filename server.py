from flask import Flask, abort, request
from flask_restful import Resource, Api
from GPI import fuzzyLogic

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        name = request.form['name']
        password = request.form['password']
        fuzzyLogic(request.form)
        return { 'name': name, 'password': password }

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)