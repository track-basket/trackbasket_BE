import pytest
import os

from tests.support.configure_test import app
from trackbasket_be.config import (
    TestingConfig,
    DevelopmentConfig,
    ProductionConfig,
)


@pytest.mark.skipif(
    "TRAVIS" in os.environ and os.environ["TRAVIS"] == "True",
    reason="Skipping this test on Travis CI.",
)

def test_development_config(app):
    app = app(DevelopmentConfig)
    assert app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == os.environ['DATABASE_URL']


def test_testing_config(app):
    app = app(TestingConfig)
    assert app.config["DEBUG"]
    assert app.config["TESTING"]
    assert not app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == os.environ['TEST_DATABASE_URL']

def test_production_config(app):
    app = app(ProductionConfig)
    assert not app.config["DEBUG"]
    assert not app.config["TESTING"]
    assert app.config["SQLALCHEMY_DATABASE_URI"] == os.environ['DATABASE_URL']