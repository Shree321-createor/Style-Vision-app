from tests.conftest import http_client


def test_search_clothing_items():

    response = http_client.get(
        "/items/search?q=dress"
    )

    assert response.status_code == 200
