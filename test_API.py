import nose
import requests



BASE_URL = 'https://jsonplaceholder.typicode.com'
ROUTE_ALBUMS = "/albums"

STATUS_CODE_200 = 200


# ALBUMS TESTS
response_albums = requests.get(BASE_URL + ROUTE_ALBUMS)

def test_albums_status_code_funtional():
    """
    Checks that Albums route status is correct as expected.
    """
    assert response_albums.status_code == STATUS_CODE_200