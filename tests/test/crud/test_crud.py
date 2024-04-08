import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class TestCRUDBooking(object):
    @pytest.fixture()
    def create_token(self):
        response = post_request(
            url=APIConstants.url_create_token(),
            headers=Util().common_headers_json(),
            auth=None,
            payload=payload_create_token(),
            in_json=False)
        token = response.json()["token"]
        verify_json_key_for_not_null_token(key=token)
        verify_http_status_code(response_data=response, expect_data=200)
        return token

    @pytest.fixture()
    def get_booking(self):
        response = post_request(
            url=APIConstants.url_create_booking(),
            headers=Util().common_headers_json(),
            auth=None,
            payload=payload_create_booking(),
            in_json=False)
        booking_id = response.json()["bookingid"]
        verify_json_key_for_not_null(key=booking_id)
        verify_http_status_code(response_data=response, expect_data=200)
        return booking_id

    @allure.title("Test CRUD operation Update(PUT)")
    @allure.description("Verify that Full Update with the booking ID and Token is working.")
    def test_update_booking_id_token(self, create_token, get_booking):
        booking_id = get_booking
        token = create_token
        response = put_requests(
            url=APIConstants().url_patch_put_delete(booking_id=booking_id),
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=200)
        verify_response_key_should_not_be_none(key=response.json()["firstname"])
        verify_response_key_should_not_be_none(key=response.json()["lastname"])
        verify_response_key(key=response.json()["firstname"], expected_data="Kalyani")
        verify_response_key(key=response.json()["lastname"], expected_data="Potu")


    @allure.title("Test CRUD operation Delete(DELETE)")
    @allure.description("Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id_token(self, create_token, get_booking):
        booking_id = get_booking
        token = create_token
        response = delete_requests(
            url=APIConstants().url_patch_put_delete(booking_id=booking_id),
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=201)
        verify_response_delete(response=response.text)