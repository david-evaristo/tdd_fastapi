from tests.factories import product_data
from fastapi import status


async def test_controller_create_should_return_success(client, products_url):
    # breakpoint()
    response = await client.post(products_url, json=product_data())
    response.json()

    # del content["created_at"]
    # del content["updated_at"]
    # del content["id"]
    assert response.status_code == status.HTTP_201_CREATED
    # assert content == {
    #     "name": "Iphone 14 Pro Max",
    #     "quantity": 10,
    #     "price": "8.500",
    #     "status": True,
    # }
