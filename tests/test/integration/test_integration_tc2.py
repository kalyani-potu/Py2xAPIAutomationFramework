import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

class TestDeleteGetBooking(object):
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
    def create_booking(self):
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

    @allure.title("Test Delete Booking with ID and Verify using GET request")
    @allure.description("Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.")
    def test_delete_booking_id_token(self, create_token, create_booking):
        booking_id = create_booking
        token = create_token
        response = delete_requests(
            url=APIConstants().url_patch_put_delete(booking_id=booking_id),
            headers=Util().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=201)
        verify_response_delete(response=response.text)
        get_response = get_request(
            url=APIConstants().url_patch_put_delete(booking_id=booking_id),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=get_response,expect_data=404)

    # @allure.title("Test CRUD operation Get(GET)")
    # @allure.description("Verify booking is not found")
    # def test_get_booking(self,create_booking):
    #     booking_id = create_booking
    #     response = get_request(
    #         url=APIConstants().url_patch_put_delete(booking_id=booking_id),
    #         auth=None,
    #         in_json=False
    #     )
    #     verify_http_status_code(response_data=response,expect_data=200)