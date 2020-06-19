from flask_restful import Resource, reqparse, request
from ..models.volunteer import Volunteer, db
from ..models.basemodel import BaseModel

class Volunteers(Resource):

  def get(self,id):
    volunteer = Volunteer.find_by_id(id)
    if volunteer is None:
      return {'data': { 'id': 'volunteer', 'attributes': {'error': "Volunteer not found"} } }, 400
    return {'data': { 'id': 'volunteer', 'attributes': {'id': volunteer.volunteer_id, 'name': volunteer.name, 'phone number': volunteer.phone_number} } }, 200

  def post(self, id):
    if Volunteer.find_by_id(id):
      return {'data': { 'id': 'volunteer', 'attributes': {'error': "Volunteer already exists"} } }, 400
    data = request.json
    volunteer = Volunteer(name = data['name'], phone_number = data['phone_number'], volunteer_id = id)
    volunteer.save()
    return {'data': { 'id': 'volunteer', 'attributes': {'id': volunteer.volunteer_id, 'name': volunteer.name, 'phone number': volunteer.phone_number} } }, 201

  def patch(self, id):
    volunteer = Volunteer.find_by_id(id)
    if volunteer is None:
      return {'data': { 'id': 'volunteer', 'attributes': {'error': "Volunteer not found"} } }, 400
    data = request.json
    volunteer.set_attrs(name = data['name'], phone_number= data['phone_number'])
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
