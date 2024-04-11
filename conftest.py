import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

@pytest.fixture(scope="session") #fixture is destroyed at the end of the session
def create_token():
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


@pytest.fixture(scope="session")
def get_booking():
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

#if don't pass the scope, default scope is function, it is destroyed at the end of each test,
# example, when there is booking id in two test cases, booking id will be different in 2 test cases, get_booking will be called 2 times because the fixture will be destroyed at the end of each test.
########################################################################################################################
# Fixture scopes :
# Fixtures are created when first requested by a test, and are destroyed based on their scope:

# function: the default scope, the fixture is destroyed at the end of the test.
#
# class: the fixture is destroyed during teardown of the last test in the class.
#
# module: the fixture is destroyed during teardown of the last test in the module.
#
# package: the fixture is destroyed during teardown of the last test in the package.
#
# session: the fixture is destroyed at the end of the test session.