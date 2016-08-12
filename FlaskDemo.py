from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask.ext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'FlaskDemo'

mysql.init_app(app)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'Message': 'Hello World'}

class AddNewName(Resource):
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, help='Name to add new name')
		args = parser.parse_args()

		return {'Message': 'Add '+args['name']+' Success!!'}

class CreateNewPokemon(Resource):
	def post(self):
			parser = reqparse.RequestParser()
			parser.add_argument('name', type=str, help='Name to create Pokemon name')
			parser.add_argument('cp', type=str, help='Cp to create cp of Pokemon')
			args = parser.parse_args()

			conn = mysql.connect()
			cursor = conn.cursor()
			cursor.callproc('spCreatePokemon',(args['name'],args['cp']))
			data = cursor.fetchall()

			if len(data) is 0:
				conn.commit()
				return {'Message': 'Pokemon creation success'}
			else:
				return {'Message': 'Fail'}



api.add_resource(HelloWorld, '/HelloWorld')
api.add_resource(AddNewName, '/AddNewName')
api.add_resource(CreateNewPokemon, '/CreateNewPokemon')

if __name__ == '__main__':
    app.run(debug=True)

