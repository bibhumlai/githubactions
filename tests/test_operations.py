from src.maths import app

def test_home():
    reponse = app.test_client.get("/")

    assert reponse.status_code == 200
    assert response.data == b"Hello World!"