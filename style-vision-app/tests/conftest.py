import sys
from fastapi.testclient import TestClient
from pathlib import Path

project_root = Path(__file__).parent.parent

sys.path.append(str(project_root))

from app.main import app

http_client = TestClient(app)
