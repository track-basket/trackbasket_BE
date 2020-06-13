from flask_restful import Resource, reqparse, request
from ..models.volunteer import Volunteer, db
from ..models.basemodel import BaseModel

class Volunteers(Resource):

  def get(self,id):
    volunteer = db.session.query(Volunteer).filter_by(volunteer_id=id).first()
    if volunteer is None:
      return {'data': { 'id': 'volunteer', 'attributes': {'error': "Volunteer not found"} } }, 400
    else:  
      return {'data': { 'id': 'volunteer', 'attributes': {'id': volunteer.volunteer_id, 'name': volunteer.name, 'phone number': volunteer.phone_number} } }, 200

  def post(self, id):
    request_data = request.json
    if Volunteer.query.filter_by(volunteer_id=id).first() is None:
      volunteer = Volunteer(name=request_data['name'], phone_number=request_data['phone_number'], volunteer_id=id)
      db.session.add(volunteer)
      db.session.commit()
      return {'data': { 'id': 'volunteer', 'attributes': {'id': volunteer.volunteer_id, 'name': volunteer.name, 'phone number': volunteer.phone_number} } }, 201
    else:
      return {'data': { 'id': 'volunteer', 'attributes': {'error': "Volunteer already exists"} } }, 400

  def patch(self, id):
    request_data = request.json
    volunteer = db.session.query(Volunteer).filter_by(volunteer_id=id).first()
    if volunteer is None:
      return {'data': { 'id': 'volunteer', 'attributes': {'error': "Volunteer not found"} } }, 400
    else:
      request_data = request.json
      volunteer.name = request_data['name']
      volunteer.phone_number = request_data['phone_number']
      db.session.commit()
      return {'data': { 'id': 'volunteer', 'attributes': {'id': volunteer.volunteer_id, 'name': volunteer.name, 'phone number': volunteer.phone_number} } }, 200

  def delete(self, id):
    volunteer = db.session.query(Volunteer).filter_by(volunteer_id=id)
    if volunteer.first() is None:
      return {'data': { 'id': 'volunteer', 'attributes': {'error': "volunteer does not exist"} } }, 400  
    else:
      volunteer.delete()
      db.session.commit()
    return {'data': { 'id': 'volunteer', 'attributes': {'message': "volunteer with id {} successfully deleted".format(id)} } }, 200
