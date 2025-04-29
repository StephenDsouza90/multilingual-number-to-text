from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

# Basic functionality tests
def test_convert_number_to_text_success():
    response = client.post("/convert", json={"number": 123, "language": "en"})
    assert response.status_code == 200
    assert response.json() == {
        "number": 123,
        "text": "one hundred and twenty-three",
        "language": "en",
    }


# Language-specific tests
def test_convert_number_to_text_spanish():
    response = client.post("/convert", json={"number": 123, "language": "es"})
    assert response.status_code == 200
    assert response.json() == {
        "number": 123,
        "text": "ciento veintitrés",
        "language": "es",
    }


def test_convert_number_to_text_french():
    response = client.post("/convert", json={"number": 123, "language": "fr"})
    assert response.status_code == 200
    assert response.json() == {
        "number": 123,
        "text": "cent vingt-trois",
        "language": "fr",
    }


def test_convert_number_to_text_german():
    response = client.post("/convert", json={"number": 123, "language": "de"})
    assert response.status_code == 200
    assert response.json() == {
        "number": 123,
        "text": "einhundertdreiundzwanzig",
        "language": "de",
    }


# Decimal number tests
def test_convert_decimal_number_to_text():
    response = client.post("/convert", json={"number": 123.45, "language": "en"})
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {
        "number": 123.45,
        "text": "one hundred and twenty-three and forty-five cents",
        "language": "en",
    }


def test_convert_decimal_number_to_text_spanish():
    response = client.post("/convert", json={"number": 123.45, "language": "es"})
    assert response.status_code == 200
    assert response.json() == {
        "number": 123.45,
        "text": "ciento veintitrés y cuarenta y cinco centavos",
        "language": "es",
    }


def test_convert_decimal_number_to_text_french():
    response = client.post("/convert", json={"number": 123.45, "language": "fr"})
    assert response.status_code == 200
    assert response.json() == {
        "number": 123.45,
        "text": "cent vingt-trois et quarante-cinq centimes",
        "language": "fr",
    }


def test_convert_decimal_number_to_text_german():
    response = client.post("/convert", json={"number": 123.45, "language": "de"})
    assert response.status_code == 200
    assert response.json() == {
        "number": 123.45,
        "text": "einhundertdreiundzwanzig und fünfundvierzig Cent",
        "language": "de",
    }


# Error handling tests
def test_convert_number_to_text_unsupported_language():
    response = client.post("/convert", json={"number": 123, "language": "xx"})
    assert response.status_code == 400


def test_convert_number_to_text_missing_number():
    response = client.post("/convert", json={"language": "en"})
    assert response.status_code == 422


def test_convert_number_to_text_missing_language():
    response = client.post("/convert", json={"number": 123})
    assert response.status_code == 422


def test_convert_number_to_text_invalid_input():
    response = client.post("/convert", json={"number": "invalid", "language": "en"})
    assert response.status_code == 422
