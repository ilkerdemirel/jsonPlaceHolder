import nose
import requests
from nose.plugins.attrib import attr
from nose.tools import assert_false, assert_true
import re

BASE_URL = 'https://jsonplaceholder.typicode.com'

# Albums Dataset
ROUTE_ALBUMS = "/albums"
TOTAL_NUMBER_ALBUMS = 100

# Users Dataset
ROUTE_USERS = "/users"
TOTAL_NUMBER_USERS = 10

# Status Codes
# For the detailed information, please refer to
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
STATUS_CODE_200 = 200
#STATUS_CODE_400 = 400
#STATUS_CODE_404 = 404

TOTAL_NUMBER_STRESS_LOOP = 20
TOTAL_NUMBER_PERFORMANCE_LOOP = 20
RESPONSE_TIME = 5 # In Seconds
EMPTY_VALUES = ['', ' ', None]
EMAIL_REGEXP = r'[\S.]+@[\S.]+'

# ALBUMS TESTS
response_albums = requests.get(BASE_URL + ROUTE_ALBUMS)

@attr('functional', 'albums')
def test_albums_status_code_funtional():
    """
    test_albums_status_code_funtional() - A simple test checks /albums status
    @parameters : 
    response_albums.status_code : Status Code from Albums Route
    STATUS_CODE_200 = OK
    """
    assert response_albums.status_code == STATUS_CODE_200

@attr('stress', 'albums')
def test_albums_status_code_stress():
    """
    test_albums_status_code_stress() - Gets/Checks /albums status TOTAL_NUMBER_STRESS_LOOP times.
    @parameters : 
    response_albums.status_code : Status Code from Albums Route
    STATUS_CODE_200 = OK
    """
    print('Starting test_albums_status_code_stress test ...')
    for i in range(TOTAL_NUMBER_STRESS_LOOP):
        response = requests.get(BASE_URL + ROUTE_ALBUMS)
        print('{}. Response has been received..!'.format(i))
        assert response.status_code == STATUS_CODE_200

@attr('functional', 'albums')
def test_albums_total_number():
    """
    Verifies total number of albums.
    """
    data = response_albums.json()
    assert len(data) == TOTAL_NUMBER_ALBUMS

@attr('functional', 'albums')
def test_albums_verify_title():
    """
    Verifies that album title is not None or empty ''.
    """
    data = response_albums.json()
    for album in data:
        print('Album title is : {}'.format(album['title']))
        assert_false (album['title'] in EMPTY_VALUES)

@attr('performance', 'albums')
def test_albums_get_response_time():
    """
    test_albums_get_response_time() - Verifies response time in TOTAL_NUMBER_PERFORMANCE_LOOP times.
    """
    print('Starting test_albums_get_response_time test ...')
    for _ in range(TOTAL_NUMBER_PERFORMANCE_LOOP):
        response = requests.get(BASE_URL + ROUTE_ALBUMS)
        print('Response elapsed is : {}'.format(response.elapsed.total_seconds()))
        assert_true (response.elapsed.total_seconds() <= RESPONSE_TIME)

# USERS TESTS
response_users = requests.get(BASE_URL + ROUTE_USERS)

@attr('functional', 'users')
def test_users_status_code_funtional():
    """
    Checks that Users route status is correct as expected.
    """
    assert response_users.status_code == STATUS_CODE_200

@attr('stress', 'users')
def test_users_status_code_stress():
    """
    Tests User route status TOTAL_NUMBER_STRESS_LOOP times.
    """
    print('Starting test_users_status_code_stress test ...')
    for i in range(TOTAL_NUMBER_STRESS_LOOP):
        response = requests.get(BASE_URL + ROUTE_USERS)
        print('{}. Response has been gathered..!'.format(i))
        assert response.status_code == STATUS_CODE_200

@attr('performance', 'users')
def test_users_get_response_time():
    """
    test_users_get_response_time() - Verifies response time in TOTAL_NUMBER_PERFORMANCE_LOOP times.
    """
    print('Starting test_users_get_response_time test ...')
    for _ in range(TOTAL_NUMBER_PERFORMANCE_LOOP):
        response = requests.get(BASE_URL + ROUTE_USERS)
        print('Response elapsed is : {}'.format(response.elapsed.total_seconds()))
        assert_true (response.elapsed.total_seconds() <= RESPONSE_TIME)

@attr('functional', 'users')
def test_users_total_number():
    """
    Verifies total number of users.
    """
    data = response_users.json()
    assert len(data) == TOTAL_NUMBER_USERS

@attr('functional', 'users')
def test_users_verify_name():
    """
    Verifies that Users' Names are not None or empty ''.
    """
    data = response_users.json()
    for user in data:
        print('Name of user is : {}'.format(user['name']))
        assert_false (user['name'] in EMPTY_VALUES)

@attr('functional', 'users')
def test_users_verify_username():
    """
    Verifies that Users' usernames are not None or empty ''.
    """
    data = response_users.json()
    for user in data:
        print('Username of user is : {}'.format(user['username']))
        assert_false (user['username'] in EMPTY_VALUES)

@attr('functional', 'users')
def test_users_is_email_valid():
    """
    Verifies that Users' emails are in valid format.
    """
    data = response_users.json()
    for user in data:
        print('Email of user is : {}'.format(user['email']))
        assert re.match(EMAIL_REGEXP, 'test@test.com')

if __name__ == '__main__':  
    nose.run()
    print('Tests are completed!!!')