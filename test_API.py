import nose
import requests
from nose.plugins.attrib import attr
from nose.tools import assert_false

BASE_URL = 'https://jsonplaceholder.typicode.com'
ROUTE_ALBUMS = "/albums"

STATUS_CODE_200 = 200
TOTAL_NUMBER_STRESS_LOOP = 20
TOTAL_NUMBER_ALBUMS = 100
EMPTY_VALUES = ['', ' ', None]

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
