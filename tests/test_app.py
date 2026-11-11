from fastapi.testclient import TestClient

from app.main import create_app


def test_health_without_external_services(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    client = TestClient(create_app())
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_static_files_do_not_shadow_api_or_expose_parent(tmp_path):
    assets = tmp_path / "static"
    assets.mkdir()
    (assets / "index.html").write_text("<h1>App de teste</h1>", encoding="utf-8")
    (tmp_path / "private.txt").write_text("sentinel", encoding="utf-8")
    client = TestClient(create_app(assets))
    assert "App de teste" in client.get("/").text
    assert client.get("/api/health").json() == {"status": "ok"}
    assert client.get("/api/inexistente").status_code == 404
    response = client.get("/%2e%2e/private.txt")
    assert response.status_code == 404
    assert "sentinel" not in response.text


def test_internal_files_and_api_schema_are_not_published():
    client = TestClient(create_app())
    for path in ["/.env", "/AGENTS.md", "/docs", "/openapi.json"]:
        assert client.get(path).status_code == 404
