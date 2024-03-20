import pytest 
from fastapi import status

from app.test.client_cfg import client

first_user = {
    "first_name": "firstname",
    "last_name": "primero",
    "email": "first@mail.com",
    "password": "firstpass01"
}

@pytest.mark.anyio
def test_create_new_user():
    res = client.post("/user/create",json=first_user)
    assert res.status_code ==  status.HTTP_202_ACCEPTED

@pytest.mark.anyio
def test_find_user_by_email():
    email = first_user.get("email")
    res = client.get(url=f"/user/find/{email}")
    assert res.status_code == status.HTTP_200_OK