from unittest import TestCase
from app import app
from db import db

class BaseTest(TestCase):
    def setUp(self):
        # Make sure db exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite:///'
        with app.app_context():
            db.init_app(app)
            db.create_all()
        # Get a test client
        self.app = app.test_client()
        self.app_context = app.app_context

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()