import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

class TestCreateDeleteBooking(object):
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
    @allure.title("Verify Create a Booking and Delete the Booking")
    @allure.description("Creating a Booking and delete the booking")
    def test_create_delete_booking(self,create_token):
        response = post_request(
            url=APIConstants.url_create_booking(),
            headers=Util().common_headers_json(),
            auth=None,
            payload=payload_create_booking(),
            in_json=False
        )
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

        #Delete the booking
        token = create_token
        del_response = delete_requests(
            url=APIConstants().url_patch_put_delete(booking_id=booking_id),
            headers=Util().common_header_put_delete_patch_cookie(token),
            auth=None,
            in_json=False
            )
        verify_http_status_code(response_data=del_response, expect_data=201)