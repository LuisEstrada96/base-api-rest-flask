from flask_restful import Resource, request
from flask import jsonify, request as req, current_app as app
from libs.auth import auth
from libs.logger import Logger
from libs.mongo import DB
from bson.json_util import dumps

class Respondent(Resource):
    #method_decorators = [auth] # If you want apply to some method use: {'post': [auth],'put': [auth]}
    def __init__(self):
        self.log = Logger()
        self.db = DB().client
    def get(self, name=None):
        self.log.info('example info')
        self.log.debug('example debug')
        self.log.silly(name)
        self.log.warn('example warn')
        self.log.error('example error')
        match = {}
        if name: 
            match = { "firstName":name }
   
        respondents = self.db.respondents.find(match)
        if respondents:
            return jsonify(code=200, data=dumps(respondents))
        else:
            return None, 400

   
    