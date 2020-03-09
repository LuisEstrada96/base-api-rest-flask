from flask_restful import Resource, request
from flask import jsonify, request as req, current_app as app
from libs.auth import auth
from libs.logger import Logger
from libs.mongo import DB
from bson.json_util import dumps, loads, default

class Respondent(Resource):
    #method_decorators = [auth] # If you want apply to some method use: {'post': [auth],'put': [auth]}
    def __init__(self):
        self.log = Logger()
        self.db = DB().client
    def get(self, name=None):
        if(name):
            typeGet = "GET ONE"
            respondents = self.db.respondents.find_one({"firstName":name})
        else:
            typeGet = "GET ALL"
            respondents = self.db.respondents.find({})

        if (typeGet=="GET ALL" and respondents.count() > 0) or (typeGet == "GET ONE" and respondents):
            return jsonify(code=200, type=typeGet, data=dumps(respondents))
        else:
            return None, 400

    def post(self):
        self.log.info('This a example info')
        self.log.debug('This a example debug')
        self.log.silly(request.form)
        self.log.warn('This is a example warn')
        self.log.error('This is a example error')
        return request.form

   
    