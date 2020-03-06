from flask_restful import Resource, request
from wtforms import Form, validators, StringField, PasswordField
from flask import jsonify, request as req
from libs.auth import auth

class Respondent(Resource):
    method_decorators = [auth] # If you want apply to some method use: {'post': [auth],'put': [auth]}
    def get(self, id=-1):
        if(id>-1):
            typeGet = "GET ONE"
        else:
            typeGet = "GET ALL"
        return jsonify(type=typeGet,code=200)

    def post(self):
        return request.form

   
    