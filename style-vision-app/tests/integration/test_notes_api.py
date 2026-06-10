from tests.conftest import http_client


def test_add_designer_note():

    payload = {
        "item_id": 1,
        "remark": "Unique stitching detail"
    }

    response = http_client.post(
        "/notes",
        json=payload
    )

    assert response.status_code == 200

    body = response.json()

    assert body["item_id"] == 1

    assert body["remark"] == "Unique stitching detail"
