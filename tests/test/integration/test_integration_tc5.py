import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

class TestInvalidPayload(object):
    @pytest.mark.nagative
    @allure.title("Verify that Create Booking Status with wrong payload")
    @allure.description("Creating a Booking from the payload and verify the 500 status code")
    def test_create_booking_negative(self):
        response = post_request(url=APIConstants.url_create_booking(),
                                headers=Util().common_headers_json(),
                                auth=None,
                                payload={"aaa":123},
                                in_json=False)
        verify_http_status_code(response_data=response, expect_data=500)
