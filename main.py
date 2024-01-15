from flask import Flask
from flask_restful import Api, Resource
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'data': 'Hello World'}
    def post(self):
        return {'data': 'Hello World --post'}



api.add_resource(HelloWorld, '/helloworld/<string:name>')



# check weather the script is being run as the main program
if __name__ == "__main__":
    app.run(debug=True)

