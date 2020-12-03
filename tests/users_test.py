import pytest
import requests


# Requirement: user should be able to register
def test_user_register_status_code_equals_200():
    response = requests.post("https://bhmlabs.ca/api/srss/user", json={'name' : 'Admin User', 'email': 'admin@admin.com', 'password': 'admin123'})
    assert response.status_code == 201


# Requirement: user should be able to login with valid details
def test_user_login_with_valid_details():

    response = requests.post("https://bhmlabs.ca/api/srss/login",
                             json={'email': 'admin@admin.com', 'password': 'admin123'})
    response_body = response.json()
    assert response_body["message"] == "login successful"


# Requirement: user should not be able to login with invalid details
def test_user_login_with_invalid_details():

    response = requests.post("https://bhmlabs.ca/api/srss/login",
                             json={'email': 'admin@wrong.com', 'password': 'admin123'})
    response_body = response.json()
    assert response_body["message"] == "login failed"


# Requirement: user should be able to receive reset password link
def test_user_should_be_able_to_reset_password():

    response = requests.get("https://bhmlabs.ca/api/srss/password/reset",
                             json={'email': 'admin@admin.com'})
    response_body = response.json()
    assert "reset/password/admin@admin.com" in response_body["reset_link"]


# Requirement: user should be able to search a property
# Requirement: user should be able to see a property
def test_user_should_be_able_to_search():

    response = requests.get("https://bhmlabs.ca/api/srss/property/show",
                             json={'address': '20 bay st'})
    response_body = response.json()
    assert "20 bay st" in response_body["message"]


# Requirement: user should be able to apply search filters
def test_user_should_be_able_to_apply_search_filters():

    response = requests.get("https://bhmlabs.ca/api/srss/property/search/filter",
                             json={'filter': 'beds', 'value' : '4'})
    response_body = response.json()
    assert "beds" in response_body["filter"]


#Requirement: On the listing page user must also see list of schools, hospitals and local businesses near the property.
def test_user_should_get_list_of_schools_near_a_property():

    response = requests.get("https://bhmlabs.ca/api/srss/property/schools",
                             json={'address': '20 bay'})
    assert response.status_code == 200


#Requirement: On the listing page user must also see list of schools, hospitals and local businesses near the property.
def test_user_should_get_list_of_hospitals_near_a_property():
    response = requests.get("https://bhmlabs.ca/api/srss/property/hospitals",
                            json={'address': '20 bay'})
    assert response.status_code == 200


#Requirement: On the listing page user must also see list of schools, hospitals and local businesses near the property.
def test_user_should_get_list_of_local_businesses_near_a_property():
    response = requests.get("https://bhmlabs.ca/api/srss/property/businesses",
                            json={'address': '20 bay'})
    assert response.status_code == 200


