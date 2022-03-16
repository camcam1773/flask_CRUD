import os
import sys
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..')
sys.path.append(mymodule_dir)
import pytest
import app


@pytest.fixture
def client():
    db_name = "pytest.db"
    app.app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(db_name)
    app.app.config['TESTING'] = True

    app.db.create_all()
    with app.app.test_client() as client:
        yield client
    app.db.drop_all()
