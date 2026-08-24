import os
os.environ["DATABASE_URL"] = "sqlite:///./test_visitor_system.db"
import pytest
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
@pytest.fixture(scope="session", autouse=True)
def cleanup_test_db():
    yield
    from app.core.database import engine
    engine.dispose()

    db_path = "./test_visitor_system.db"
    if os.path.exists(db_path):
        try:
            os.remove(db_path)
        except PermissionError:
            pass