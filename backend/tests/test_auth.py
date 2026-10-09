from tests.conftest import client
def test_signup():
    data = {
        "name": "Test Visitor",
        "email": "test.visitor@example.com",
        "phone": "9999999999",
        "password": "TestPass123"
    }
    response = client.post("/api/auth/signup", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["success"] is True
    assert "visitor_id" in result["data"]
def test_login():
    signup_data = {
        "name": "Login Visitor",
        "email": "login.visitor@example.com",
        "phone": "8888888888",
        "password": "LoginPass123"
    }
    client.post("/api/auth/signup", json=signup_data)
    login_data = {
        "email": "login.visitor@example.com",
        "password": "LoginPass123"
    }
    response = client.post("/api/auth/login", json=login_data)
    assert response.status_code == 200
    assert response.json()["success"] is True
def test_wrong_password():
    signup_data = {
        "name": "Wrong Password",
        "email": "wrongpass.visitor@example.com",
        "phone": "7777777777",
        "password": "CorrectPass123"
    }
    client.post("/api/auth/signup", json=signup_data)
    login_data = {
        "email": "wrongpass.visitor@example.com",
        "password": "IncorrectPass"
    }
    response = client.post("/api/auth/login", json=login_data)
    assert response.status_code != 200 or response.json()["success"] is False