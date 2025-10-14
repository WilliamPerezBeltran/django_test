# Emissions Backend

This document provides an overview of the Emissions backend project. It includes architecture, design principles, API endpoints, testing practices, and Docker setup. This README is intended for developers and engineers who want to understand, run, and extend the backend application.

## Project Description

The Emissions backend manages emission data for different countries, years, and activities. The data is stored in a database and exposed via a REST API. The project is structured to separate domain logic, infrastructure, and API layers:

* **Domain**: Contains entities (`Emission`) and abstract repositories (`EmissionRepository`) that define core business logic.
* **Infrastructure**: Contains Django models, serializers, views, and repository implementations.
* **Use Cases**: Contains application logic such as fetching emissions.
* **Tests**: Validates the behavior of domain, infrastructure, and use cases.

This architecture ensures modularity, testability, and maintainability.

## Stack

* Python 3.8
* Django 4.2
* SQLite3
* Docker & Docker Compose

## Architecture Explanation

* **Domain Layer**: Defines core entities and abstractions.
* **Infrastructure Layer**: Implements Django models, API views, and serializers.
* **Use Cases Layer**: Handles business logic and orchestration between domain and infrastructure.

This separation ensures **Single Responsibility Principle (SRP)** and allows adding features without modifying existing code (**Open/Closed Principle**). The repository pattern decouples domain logic from Django ORM (**Dependency Inversion Principle**).

## SOLID Principles Applied

* **SRP**: Each class has a single responsibility (entity, repository, API view, or use case).
* **OCP**: New use cases or rules can be added without modifying domain classes.
* **LSP**: Entities can be replaced with compatible objects.
* **ISP**: Interfaces expose only necessary methods (`EmissionRepository.list`).
* **DIP**: Views and use cases depend on abstractions, not concrete models.

## Design Patterns

* **Repository Pattern**: `EmissionRepository` defines an abstraction for persistence; implemented in `repository_impl.py`.
* **Factory/Builder Pattern**: Use cases in `usecases/get_emissions.py` construct domain objects from models.
* **Strategy Pattern**: Supports different strategies for filtering or calculating emissions.

## API Endpoints

| Method | URL               | Description                     | Filters                                        |
| ------ | ----------------- | ------------------------------- | ---------------------------------------------- |
| GET    | `/`               | Returns `"Backend is running!"` | N/A                                            |
| GET    | `/admin/`         | Django admin panel              | N/A                                            |
| GET    | `/api/emissions/` | Returns a list of emissions     | `year`, `country`, `emission_type`, `activity` |

### Example Requests Using cURL

* Get all emissions:

```bash
curl -X GET http://localhost:8000/api/emissions/
```

* Filter by year:

```bash
curl -X GET "http://localhost:8000/api/emissions/?year=2020"
```

* Filter by country:

```bash
curl -X GET "http://localhost:8000/api/emissions/?country=Colombia"
```

* Filter by emission type:

```bash
curl -X GET "http://localhost:8000/api/emissions/?emission_type=CO2"
```

* Filter by multiple parameters:

```bash
curl -X GET "http://localhost:8000/api/emissions/?year=2020&country=Colombia&emission_type=CO2"
```

## Project Structure

```tree
.
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── emissions_project
│   ├── asgi.py
│   ├── domain
│   │   ├── entities.py
│   │   └── repositories.py
│   ├── infrastructure
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── repository_impl.py
│   │   ├── serializers.py
│   │   └── views.py
│   ├── urls.py
│   ├── usecases
│   │   └── get_emissions.py
│   ├── settings.py
│   └── wsgi.py
├── manage.py
├── README.md
└── requirements.txt
```

### Folder Description

* `domain/` -> Entities and repository interfaces.
* `infrastructure/` -> Django models, views, serializers, and repository implementations.
* `usecases/` -> Application logic for fetching or processing emissions.
* `tests/` -> Unit and integration tests.

### File Description

* `entities.py` -> Emission dataclass.
* `repositories.py` -> Abstract repository interface.
* `models.py` -> Django model for Emission.
* `repository_impl.py` -> Concrete implementation using Django ORM.
* `serializers.py` -> DRF serializers.
* `views.py` -> API views.
* `get_emissions.py` -> Use case to fetch emissions.
* `urls.py` -> API routes.
* `tests/` -> Unit and integration tests.

## Docker Setup

### Dockerfile

```dockerfile
FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### docker-compose.yml

```yaml
version: '3.9'
services:
  backend:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/usr/src/app
    environment:
      - PYTHONUNBUFFERED=1
```

### Running Docker

Build and start containers:

```bash
docker-compose up --build
```

Stop containers:

```bash
docker-compose down
```

## Testing

The project uses Django’s test framework.

Run all tests:

```bash
docker-compose run backend python manage.py test
```

Run a specific test file:

```bash
docker-compose run backend python manage.py test emissions_project.tests.test_emissions_api
```

## Development Practices

* **TDD**: Test-driven development for reliable and maintainable code.
* **Dockerized**: All dependencies are containerized for reproducible development environments.
* **Code Quality**: PEP8 and Pythonic standards followed.

## Author

**William Pérez**

* [GitHub profile](https://github.com/WilliamPerezBeltran)
