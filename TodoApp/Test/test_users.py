from TodoApp.Test.utils import *
from TodoApp.routers.users import get_current_user, get_db
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users/get_user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()['username'] == "codingwithjedtest"
    assert response.json()['email'] == "codingwithjedtest@email.com"
    assert response.json()['first_name'] == "Jed"
    assert response.json()['last_name'] == "Test"
    assert response.json()['role'] == "admin"
    assert response.json()['phone_number'] == "1234567890"

def test_change_password_success(test_user):
    reponse = client.put("/users/change_password", json={"old_password": "testpassword", "new_password": "newpassword"})
    assert reponse.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    reponse = client.put("/users/change_password", json={"old_password": "wrong_password", "new_password": "newpassword"})
    assert reponse.status_code == status.HTTP_401_UNAUTHORIZED
    assert reponse.json() == {"detail": "Error changing password"}

def test_change_phone_number_success(test_user):
    response = client.put("/users/update_phone_number", json={"phone_number": "2222222222"})
    assert response.status_code == status.HTTP_204_NO_CONTENT

