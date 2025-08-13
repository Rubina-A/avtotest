import pytest
import requests


@pytest.fixture
def base_url():
    return "https://yougile.com/api-v2"

@pytest.fixture
def auth_headers():
    return {
        "Authorization": "Bearer 1AkG5rb1khNd35U9Py6ZmhAJdyG5vMGVwYi2dDpUprmMTRnA0l6ll4gzH5KkJGxO",
        "Content-Type": "application/json"
    }


@pytest.fixture
def create_test_project(base_url, auth_headers):
    url = f"{base_url}/projects"
    data = {"title": "Test Project for API Testing"}
    response = requests.post(url, json=data, headers=auth_headers)
    project_id = response.json()["id"]
    yield project_id
    requests.put(f"{url}/{project_id}", json={"deleted": True}, headers=auth_headers)
