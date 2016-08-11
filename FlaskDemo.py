from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Message': 'Hello World'}

class AddNewName(Resource)
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, help='Name to add new name')
		args = parser.parse_args()

		return {'Message': 'Add '+args['name']+' Success !!'}


api.add_resource(HelloWorld, '/HelloWorld')

if __name__ == '__main__':
    app.run(debug=True)