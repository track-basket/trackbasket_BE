from flask_restful import Resource, reqparse, request
from models.volunteer import Volunteer, db
from models.basemodel import BaseModel

class Volunteers(Resource):

  def get(self,id):
    volunteer = db.session.query(Volunteer).get(id)
    return {'volunteer': volunteer.name}

  def post(self, id):
    request_data = request.json
    volunteer = Volunteer(name=request_data['name'], phone_number=request_data['phone_number'])
    db.session.add(volunteer)
    db.session.commit()
    # write to the database
    return {'volunteer': request_data}
