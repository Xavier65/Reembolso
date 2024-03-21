from fastapi.testclient import TestClient

from app import server

client = TestClient(
    app=server,
    headers={'accept':'application/json'}
)

