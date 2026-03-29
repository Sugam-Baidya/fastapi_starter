# 🚀 FastAPI Project

A RESTful API built with [FastAPI](https://fastapi.tiangolo.com/), SQLmodel, and Alembic for database migrations.

---

## 📋 Prerequisites

Make sure you have the following installed:

- Python 3.10+
- pip
- PostgreSQL 

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory of the project:

```bash
cp .env.example .env
```

Then update the values in `.env` with your configuration

> ⚠️ **Never commit your `.env` file to version control.** It is already listed in `.gitignore`.

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Sugam-Baidya/fastapi_starter.git
   cd fastapi_starter
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv

   # On macOS/Linux
   source venv/bin/activate

   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🗄️ Database Migrations (Alembic)

### Initialize Alembic *(only needed once)*

```bash
alembic init alembic
```

### Create a new migration

After making changes to your SQLAlchemy models, generate a new migration file:

```bash
alembic revision --autogenerate -m "your migration message"
```

### Apply migrations

Run all pending migrations to update the database schema:

```bash
alembic upgrade head
```

### Rollback migrations

Revert the last applied migration:

```bash
alembic downgrade -1
```

Revert all migrations:

```bash
alembic downgrade base
```

### Check current migration version

```bash
alembic current
```

### View migration history

```bash
alembic history --verbose
```

---

## ▶️ Running the Application

### Development mode (with auto-reload)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Production mode

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Using Python directly

```bash
python main.py
```

---

## 📖 API Documentation

Once the server is running, access the interactive API docs at:

| Interface | URL |
|-----------|-----|
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |
| OpenAPI JSON | http://localhost:8000/openapi.json |

---

## 🧪 Running Tests

```bash
pytest
```

With coverage report:

```bash
pytest --cov=app tests/
```

---

## 📄 License

This project is licensed under the [MIT License](License.md).