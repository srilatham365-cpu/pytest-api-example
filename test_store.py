from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

@pytest.fixture
def create_order():
    test_endpoint = "/store/order"
    order_data = {"pet_id": 0}
    response = api_helpers.post_api_data(test_endpoint, order_data)
    assert response.status_code == 201
    order = response.json()
    validate(instance=order, schema=schemas.order)
    return order

def test_patch_order_by_id(create_order):
    order = create_order
    order_id = order['id']
    test_endpoint = f"/store/order/{order_id}"
    update_data = {"status": "sold"}
    response = api_helpers.patch_api_data(test_endpoint, update_data)
    assert response.status_code == 200
    assert_that(response.json()['message'], is_("Order and pet status updated successfully"))
    pet_id = order['pet_id']
    pet_response = api_helpers.get_api_data(f"/pets/{pet_id}")
    assert pet_response.status_code == 200
    assert_that(pet_response.json()['status'], is_("sold"))
