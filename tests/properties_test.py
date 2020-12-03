import pytest
import requests


# Requirement: user should be able to add a new property
def test_user_can_add_property_status_code_equals_201():
    response = requests.post("https://bhmlabs.ca/api/srss/property", json={'address' : '20 bay st, toronto', 'price': '500,000 CAD', 'beds': '4', 'bath' : '2'})
    assert response.status_code == 201


# Requirement: user should be able to see a property
def test_user_can_search_a_property():

    response = requests.get("https://bhmlabs.ca/api/srss/property/show",
                             json={'address': '20 bay st'})
    response_body = response.json()
    assert "20 bay st" in response_body["message"]


