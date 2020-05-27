from flask_restful import Resource, reqparse, request

class Volunteer(Resource):

  def get(self,id):
    return {'volunteer': id}

  def post(self,id):
    request_data = request.json
    # write to the database
    return {'volunteer': request_data}
