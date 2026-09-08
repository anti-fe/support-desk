from fastapi import FastAPI


app = FastAPI(
    title="CI/CD Application",
    description="Учебное приложение для моделирования CI/CD",
    version="1.0.0",
)
# Главная страница
@app.get("/")
def root():
    return {
        "message": "CI/CD Application",
    }
# Страница /health
@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }