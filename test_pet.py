from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

def test_pet_schema():
    test_endpoint = "/pets/1"
    response = api_helpers.get_api_data(test_endpoint)
    assert response.status_code == 200
    validate(instance=response.json(), schema=schemas.pet)

@pytest.mark.parametrize("status", ["available", "sold", "pending"])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {"status": status}
    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for pet in response.json():
        assert_that(pet['status'], is_(status))
        validate(instance=pet, schema=schemas.pet)

@pytest.mark.parametrize("pet_id", [999, 100, 50])
def test_get_by_id_404(pet_id):
    test_endpoint = f"/pets/{pet_id}"
    response = api_helpers.get_api_data(test_endpoint)
    assert response.status_code == 404
    assert_that(response.json()['message'], contains_string("not found"))