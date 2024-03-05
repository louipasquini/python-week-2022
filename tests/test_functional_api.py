from fastapi.testclient import TestClient

from beerlog.api import api

client = TestClient(api)


def test_create_beer_via_api():
    response = client.post(
        "/beers/",
        json={
            "name": "Skol",
            "style": "Pilsen",
            "flavor": 5,
            "image": 8,
            "cost": 10,
        },
    )
    assert response.status_code >= 200 and response.status_code < 300
    result = response.json()
    assert result["id"] == 1
    assert result["name"] == "Skol"
    assert result["style"] == "Pilsen"
    assert result["flavor"] == 5
    assert result["image"] == 8
    assert result["cost"] == 10
