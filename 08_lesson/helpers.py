def validate_project_response(response, expected_status_code):
    assert response.status_code == expected_status_code
    if expected_status_code in (200, 201):
        data = response.json()
        assert "id" in data
        assert isinstance(data["id"], str)
        return data
    return None
