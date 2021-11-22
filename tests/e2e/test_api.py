import uuid

import httpx
import pytest


@pytest.fixture(scope="session")
def user_api():
    client = httpx.Client(base_url="http://localhost:3001")
    try:
        yield client
    finally:
        client.close()


@pytest.fixture(scope="session")
def reservation_api():
    client = httpx.Client(base_url="http://localhost:3000")
    try:
        yield client
    finally:
        client.close()


def test_create_user_and_reservation(user_api, reservation_api):
    user_create_response = user_api.post(
        "/auth/register",
        json={
            "email": "test@test.com",
            "password": "test",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
        },
    ).json()
    created_user_id = user_create_response["id"]

    reservation_create_response = reservation_api.post(
        "/reservation",
        json={
            "start_at": "2021-11-08T15:13:07.457Z",
            "end_at": "2021-11-08T16:13:07.457Z",
            "created_by": created_user_id,
            "name": "작업실 테스트 예약",
            "description": "작업실 테스트 예약 설명",
        },
    )

    assert reservation_create_response.is_success is True


def test_reservation_add_should_return_error_when_no_user_id_is_found(reservation_api):
    new_uuid_that_should_not_exist = uuid.uuid4()

    response = reservation_api.post(
        "/reservation",
        json={
            "start_at": "2021-11-08T15:13:07.457Z",
            "end_at": "2021-11-08T16:13:07.457Z",
            "created_by": str(new_uuid_that_should_not_exist),
            "name": "작업실 테스트 예약",
            "description": "작업실 테스트 예약 설명",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "유저 아이디를 찾을 수 없습니다"
