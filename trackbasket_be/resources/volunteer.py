from flask_restful import Resource, reqparse, request
from models.volunteer import Volunteer, db
from models.basemodel import BaseModel

class Volunteers(Resource):

  def get(self,id):
    volunteer = db.session.query(Volunteer).filter_by(volunteer_id=id).first()
    return {'data': { 'id': 'volunteer', 'attributes': {'id': volunteer.volunteer_id, 'name': volunteer.name, 'phone number': volunteer.phone_number} } }

  def post(self, id):
    request_data = request.json
    volunteer = Volunteer(name=request_data['name'], phone_number=request_data['phone_number'], volunteer_id=id)
    db.session.add(volunteer)
    db.session.commit()
    return {'volunteer': request_data}
