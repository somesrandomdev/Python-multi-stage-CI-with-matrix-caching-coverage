from main import app  # import the Flask app

def test_alive():
    with app.test_client() as c:
        rv = c.get("/")
        json = rv.get_json()
        assert rv.status_code == 200
        assert "I’m alive" in json["message"]