# PyCommerce

Django REST API for managing products and categories. Authenticated CRUD, product image uploads, nested categories, and filtering by title/SKU, price range, and category.

## Stack

- Python 3.14+, Django 6.1, Django REST Framework
- django-filter, drf-spectacular (OpenAPI / Swagger / ReDoc), Pillow
- SQLite for local development with [uv](https://docs.astral.sh/uv/); PostgreSQL and Gunicorn when running in Docker

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

Docker Compose runs Gunicorn against PostgreSQL.

```bash
cp .env.example .env
docker compose up --build
```

The API is at http://localhost:8000/. Health check: http://localhost:8000/healthz/.

```bash
docker compose exec web python manage.py createsuperuser
```
