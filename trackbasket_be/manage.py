from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from trackbasket_be import create_app, db
# from app import app, db

from trackbasket_be.models.volunteer import Volunteer
from trackbasket_be.models.at_risk_user import AtRiskUser
from trackbasket_be.models.conversation import Conversation
from trackbasket_be.models.message import Message
from trackbasket_be.models.basemodel import BaseModel

app = create_app("development")
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
