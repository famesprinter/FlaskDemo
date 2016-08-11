from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def post(self):
        return {'Message': 'Hello World'}

api.add_resource(HelloWorld, '/HelloWorld')

if __name__ == '__main__':
    app.run(debug=True)