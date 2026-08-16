# PyCommerce

Django REST API for managing products and categories. Authenticated CRUD, product image uploads, nested categories, and filtering by title/SKU, price range, and category.

## Stack

- Python 3.14+, Django 6.1, Django REST Framework
- django-filter, drf-spectacular (OpenAPI / Swagger / ReDoc), Pillow
- SQLite for local development, packaged with [uv](https://docs.astral.sh/uv/)

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
