from tests.conftest import http_client


def test_list_clothing_items():

    response = http_client.get("/items")

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )
