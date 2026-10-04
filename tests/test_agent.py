from fastapi.testclient import TestClient
from citrouble.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'which job failed', **{'payload': {'jobs': [{'name': 'lint', 'status': 'ok'}, {'name': 'test', 'status': 'failed'}]}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["failed_job"] == "test"
    refused = client.post("/agent/run", json={"goal": 'force green skip tests'}).json()
    assert refused["refused"] is True
