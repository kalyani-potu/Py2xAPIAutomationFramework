import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

class TestGetUpdateGetBooking(object):
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

    @allure.title("Test Update Booking with ID and Verify using GET request")
    @allure.description("Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id")
    def test_update_get_booking(self,create_token):
        #Get all bookingids
        get_all_response = get_request(
            url=APIConstants().url_get_all_booking(),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=get_all_response, expect_data=200)
        #accessing one booking id
        booking_id = get_all_response.json()[0]["bookingid"]
        print(booking_id)

        #update the details of booking id
        token = create_token
        update_response = put_requests(
            url=APIConstants().url_patch_put_delete(booking_id=booking_id),
            headers=Util().common_header_put_delete_patch_cookie(token),
            auth=None,
            payload=payload_create_booking(),
            in_json=False
        )
        verify_http_status_code(response_data=update_response, expect_data=200)

        #get the details after updating
        get_response = get_request(
            url=APIConstants().url_patch_put_delete(booking_id=booking_id),
            auth=None,
            in_json=False
        )
        verify_http_status_code(response_data=get_response,expect_data=200)
        verify_response_key(key=get_response.json()["firstname"],expected_data="Kalyani")
        verify_response_key(key=get_response.json()["lastname"],expected_data="Potu")
        verify_response_key(key=get_response.json()["totalprice"],expected_data=111)
        verify_response_key(key=get_response.json()["depositpaid"],expected_data=True)
        verify_response_key(key=get_response.json()["additionalneeds"],expected_data="Breakfast")
        verify_response_key(key=get_response.json()["bookingdates"]["checkin"],expected_data="2018-01-01")
        verify_response_key(key=get_response.json()["bookingdates"]["checkout"],expected_data="2019-01-01")
