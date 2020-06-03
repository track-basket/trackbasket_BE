import pytest

from trackbasket_be import create_app, db
from trackbasket_be.config import TestingConfig


@pytest.yield_fixture
def app():
    def _app(config_class):
        app = create_app(config_class)
        app.test_request_context().push()
        
        if config_class is TestingConfig:

            db.drop_all()
            from trackbasket_be.models.at_risk_user import AtRiskUser
            from trackbasket_be.models.volunteer import Volunteer
            from trackbasket_be.models.item import Item
            from trackbasket_be.models.shopping_list import ShoppingList
            from trackbasket_be.models.store import Store
            

            db.create_all()

        return app

    yield _app
    db.session.remove()
    if str(db.engine.url) == TestingConfig.SQLALCHEMY_DATABASE_URI:
        db.drop_all()