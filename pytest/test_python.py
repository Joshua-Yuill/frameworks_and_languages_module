import requests

ENDPOINT="https://jsonplaceholder.typicode.com/"

def test_get_post_1():
    response = requests.get(ENDPOINT + 'posts/1')
    # Find out what the request should return with
    # curl https://jsonplaceholder.typicode.com/posts/1
    # Assert the right data is returned
    data = response.json()
    assert data['id'] == 1

def test_create_post():
    ITEM={"title": "foo", "body": "bar", "userId": "1"}
    response = requests.post(ENDPOINT + 'posts', json=ITEM)
    data = response.json()
    assert data['id'] > 100

def test_delete_post_1():
    response = requests.delete(ENDPOINT + 'posts/1')
    data = response.json()
    assert response.status_code == 200