FROM node:22-bookworm-slim AS frontend
WORKDIR /build/frontend
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM ghcr.io/astral-sh/uv:0.12.13 AS uv
FROM python:3.12-slim AS runtime
COPY --from=uv /uv /usr/local/bin/uv
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 UV_NO_CACHE=1
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project
COPY app/ ./app/
COPY --from=frontend /build/app/static ./app/static/
RUN useradd --create-home --uid 10001 appuser
USER appuser
EXPOSE 8000
CMD ["/app/.venv/bin/python", "-m", "app"]
