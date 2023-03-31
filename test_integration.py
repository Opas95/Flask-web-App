from my_app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'I am almost a Devops Engineer!' in response.data
