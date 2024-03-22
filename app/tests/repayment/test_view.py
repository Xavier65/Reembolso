# REPAYMENT - CRUD
import pytest
import json
from app.tests import client

with open("app/tests/repayment/repayment_input.json", "r") as file:
    data = json.loads(file)
    file.close()


@pytest.mark.parametrize("repayment", data.get("input"))
def test_create_new_repayment(repayment: dict):
    client
