from tests.conftest import http_client


def test_filter_by_garment_type():

    response = http_client.get(
        "/items/filter?garment_type=Dress"
    )

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body, list)
