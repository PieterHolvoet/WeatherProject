import requests

def test_get_weather():
    response = requests.get('http://localhost:5000/weather?city=London')
    assert response.status_code == 200
    data = response.json()
    assert 'temperature' in data
    assert 'condition' in data
