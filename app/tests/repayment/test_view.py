# REPAYMENT - CRUD
import pytest
import json
from fastapi import status
from app.tests import client

with open("app/tests/repayment/repayment_input.json", "r") as file:
    data = json.load(file)
    file.close()


@pytest.mark.parametrize("repayment", data.get("input"))
def test_create_new_repayment(repayment: dict):
    res = client.post(url=f"/repayment/create", json=repayment)
    assert res.status_code == status.HTTP_202_ACCEPTED
