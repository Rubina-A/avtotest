import pytest
import requests
from helpers import validate_project_response


class TestProjectsAPI:


    def test_create_project_positive(self, base_url, auth_headers):
        url = f"{base_url}/projects"
        data = {"title": "New Project"}
        response = requests.post(url, json=data, headers=auth_headers)
        project_data = validate_project_response(response, 201)
        
        requests.put(f"{url}/{project_data['id']}", json={"deleted": True}, headers=auth_headers)

    def test_create_project_negative(self, base_url, auth_headers):
        url = f"{base_url}/projects"
        data = {}
        response = requests.post(url, json=data, headers=auth_headers)
        assert response.status_code == 400

    def test_get_project_positive(self, base_url, auth_headers, create_test_project):
        url = f"{base_url}/projects/{create_test_project}"
        response = requests.get(url, headers=auth_headers)
        validate_project_response(response, 200)

    def test_get_project_negative(self, base_url, auth_headers):
        url = f"{base_url}/projects/non_existent_project_id"
        response = requests.get(url, headers=auth_headers)
        assert response.status_code == 404

    def test_update_project_positive(self, base_url, auth_headers, create_test_project):
        url = f"{base_url}/projects/{create_test_project}"
        new_title = "Updated Project Title"
        data = {"title": new_title}
        response = requests.put(url, json=data, headers=auth_headers)
        updated_data = validate_project_response(response, 200)
   
    def test_update_project_negative(self, base_url, auth_headers):
        url = f"{base_url}/projects/non_existent_project_id"
        data = {"title": "Should Fail"}
        response = requests.put(url, json=data, headers=auth_headers)
        assert response.status_code == 404
