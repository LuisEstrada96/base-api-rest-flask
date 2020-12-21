from flask import Flask, request
from flask_restful import Api
from resources.respondent import Respondent
from libs.logger import Logger
from config.config import general as config
app = Flask(__name__)
api = Api(app)
log = Logger()

# Routes
api.add_resource(Respondent, '/respondent','/respondent/<name>')
#-------
if __name__ == '__main__':
    log.info('Server listen in %s:%s' %(config['host'], config['port']))
    app.run(debug=True, host=config['host'], port=config['port'])