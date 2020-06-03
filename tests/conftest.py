import pytest
from project import create_app
@pytest.fixture
def app():
    app = create_app()
    app.config.from_object('project.config.TestingConfig')
    return app