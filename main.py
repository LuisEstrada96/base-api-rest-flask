from flask import Flask, request
from flask_restful import Api
from resources.respondents.respondent import Respondent

app = Flask(__name__)
api = Api(app)

# Routes
api.add_resource(Respondent, '/respondent','/respondent/<int:id>')    # GET
#-------
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)