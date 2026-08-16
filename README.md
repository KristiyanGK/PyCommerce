# PyCommerce

Django REST API for managing products and categories. Authenticated CRUD, product image uploads, nested categories, and filtering by title/SKU, price range, and category.

## Stack

- Python 3.14+, Django 6.1, Django REST Framework
- django-filter, drf-spectacular (OpenAPI / Swagger / ReDoc), Pillow
- SQLite and local `media/` for development with [uv](https://docs.astral.sh/uv/); PostgreSQL, Gunicorn, and MinIO when running in Docker

## Layout

```
src/pycommerce/           project settings
src/product_manager/      main product management app
  models/                 Product, Category
  views/                  ModelViewSets
  serializers/
  filters/                search, min/max price, category
```

## API

Interactive docs at `/api/docs/` (Swagger) and `/api/redoc/`.

| Resource | Path |
| --- | --- |
| Products | `/api/products/` |
| Categories | `/api/categories/` |
| Admin | `/admin/` |

Product list query params: `search`, `min_price`, `max_price`, `category`.

## Run locally

```bash
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

## Run with Docker

Docker Compose runs Gunicorn against PostgreSQL. Product images are stored in MinIO.

```bash
cp .env.example .env
docker compose up --build
```

Product `image` URLs should look like `http://localhost:9000/pycommerce/products/...`. If you open the API as `http://127.0.0.1:8000/`, set `MINIO_CUSTOM_DOMAIN=127.0.0.1:9000/pycommerce` in `.env`. Re-upload images that were saved before MinIO was enabled.

The API is at http://localhost:8000/. Health check: http://localhost:8000/healthz/.
MinIO API is at http://localhost:9000/; the console is at http://localhost:9001/ (credentials from `.env`).

```bash
docker compose exec web python manage.py createsuperuser
```
