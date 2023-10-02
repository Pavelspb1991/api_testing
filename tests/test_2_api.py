from api.questions_api import api
from http import HTTPStatus
from utils.assertions import Assert


def test_2_status():
    res = api.list_users()
    assert res.status_code == HTTPStatus.OK
    # Assert.validate_schema(res_body())


def test_user_found():
    res = api.single_user()
    res_body = res.json()

    assert res.status_code == HTTPStatus.OK
    # Assert.validate_schema(res_body())

    assert res_body["data"]["first_name"] == "Janet"
    example = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    assert example == res_body


def test_user_not_found():
    res = api.single_user_not_found()
    assert res.status_code == HTTPStatus.NOT_FOUND
    # Assert.validate_schema(res.json())


def test_create():
    res = api.create("Pavel", "qa")
    assert res.status_code == HTTPStatus.CREATED
    assert res.json()['name'] == 'Pavel'
    assert res.json()['job'] == "qa"

    assert api.delete_user(res.json()["id"]).status_code == HTTPStatus.NO_CONTENT
    # Assert.validate_schema(res.json())
