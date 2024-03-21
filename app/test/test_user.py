import json
import pytest 
from fastapi import status

from app.test.client_cfg import client

with open("app/test/user_input.json","r") as file:
    data = json.load(file)

@pytest.mark.parametrize("new_user",data)
def test_create_new_user(new_user:dict):
    res = client.post("/user/create",json=new_user)
    assert res.status_code ==  status.HTTP_202_ACCEPTED

@pytest.mark.parametrize("user",data)
def test_find_user_by_email(user:dict):
    email = user.get("email")
    res = client.get(url=f"/user/find/{email}")
    assert res.status_code == status.HTTP_200_OK