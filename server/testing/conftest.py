#!/usr/bin/env python3
import pytest
from app import create_app, db

@pytest.fixture
def client():
    app = create_app(testing=True)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client







