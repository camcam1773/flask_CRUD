import os
import sys
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
import pytest
from app import create_app, db


@pytest.fixture
def client():
    db_name = "pytest.db"
    instance_dir = os.path.join(mymodule_dir, 'instance')
    db_path = os.path.join(instance_dir, db_name)

    # Clean up any leftover database file from a previous aborted run
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
        except OSError:
            pass

    test_app = create_app({
        'SQLALCHEMY_DATABASE_URI': "sqlite:///{}".format(db_name),
        'TESTING': True
    })

    with test_app.app_context():
        db.create_all()

    with test_app.test_client() as client:
        yield client

    with test_app.app_context():
        db.drop_all()

    if os.path.exists(db_path):
        try:
            os.remove(db_path)
        except OSError:
            pass
