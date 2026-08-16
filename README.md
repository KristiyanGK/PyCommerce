# PyCommerce

Django REST API for managing products and categories. 
Provides CRUD with basic auth, product image uploads (local or via MinIO) and filtering by title/SKU, price range, and category.

## Stack

- Restful endpoints via Django and Django REST Framework
- OpenAPI support via drf-spectacular
- Storage: SQLite (dev), PostgreSQL and MinIO (docker)
- Package manager: UV
- Linter/Formatter: Ruff

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

## Code formatting
```bash
uv run ruff format
```

## Run with Docker

Docker Compose runs Gunicorn against PostgreSQL. Product images are stored in MinIO.

```bash
cp .env.example .env
docker compose up --build
```

Product `image` URLs should look like `http://localhost:9000/pycommerce/products/...`.

API: http://localhost:8000/api
Health check: http://localhost:8000/healthz/.
MinIO: http://localhost:9000/, and it's console http://localhost:9001/.

Setup superuser:
```bash
docker compose exec web python manage.py createsuperuser
```
