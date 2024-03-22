# USER - crud
import json
import pytest
from fastapi import status

from app.tests import client

with open("app/tests/user/user_input.json", "r") as file:
    data = json.load(file)
    file.close()


@pytest.mark.parametrize("new_user", data.get("input"))
def test_create_new_user(new_user: dict):
    res = client.post("/user/create", json=new_user)
    assert res.status_code == status.HTTP_202_ACCEPTED


@pytest.mark.parametrize("user", data.get("input"))
def test_find_user_by_email(user: dict):
    email = user.get("email")
    res = client.get(url=f"/user/read/{email}")
    assert res.status_code == status.HTTP_200_OK


@pytest.mark.parametrize("update_user", data.get("update"))
def test_update_user_by_email(update_user: dict):
    email = update_user.get("email")
    res = client.put(url=f"/user/update/{email}", json=update_user)
    assert res.status_code == status.HTTP_200_OK


@pytest.mark.skip(reason="testing start")
@pytest.mark.parametrize("delete_user", data.get("input"))
def test_delete_user_by_email(delete_user: dict):
    email = delete_user.get("email")
    res = client.delete(url=f"/user/delete/{email}")
    assert res.status_code == status.HTTP_200_OK
