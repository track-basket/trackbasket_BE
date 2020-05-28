from .volunteer import Volunteers
from .at_risk_user import AtRiskUsers

def initialize_routes(api):
  api.add_resource(Volunteers, '/api/v1/volunteer/<string:id>')
  api.add_resource(AtRiskUsers, '/api/v1/atriskuser/<string:id>')
  