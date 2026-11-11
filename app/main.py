"""API mínima; nenhuma integração, credencial ou dado corporativo é necessário."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


def create_app(static_dir: Path | None = None) -> FastAPI:
    application = FastAPI(
        title="Capricórnio • App interno",
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
    )

    @application.get("/api/health")
    def health() -> dict[str, str]:
        # Liveness: não verifica acesso a banco ou provedor de IA.
        return {"status": "ok"}

    assets = static_dir if static_dir is not None else Path(__file__).parent / "static"
    if assets.is_dir():
        application.mount("/", StaticFiles(directory=assets, html=True), name="frontend")

    return application


app = create_app()
