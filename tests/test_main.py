from fastapi.testclient import TestClient
from app.main import app


# Создаём тестовый клиент для взаимодействия с приложением
client = TestClient(app)

def test_root():
    response = client.get("/")
    # Проверяем, что сервер вернул успешный HTTP-код
    assert response.status_code == 200
    assert response.json() == {
        "message": "CI/CD Application",
    }
def test_health_check():
    response = client.get("/health")
    # Проверяем, что сервер вернул успешный HTTP-код
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
    }