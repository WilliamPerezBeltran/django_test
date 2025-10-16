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


# Emissions Project - Docker Setup

This project uses **Docker Compose** to run the Django backend with SQLite.

## Start the Containers

```bash
docker-compose up -d
```

## Seed the Database

```bash
docker-compose exec backend python manage.py seed_emissions
```

## Verify the Data

```bash
docker-compose exec backend python manage.py shell
```

Inside the shell:

```python
from emissions_project.infrastructure.models import EmissionModel
EmissionModel.objects.count()
# Output: 100
```

## Notes

* SQLite database file `db.sqlite3` is persistent in the project folder.
* You only need to run the seed once unless you delete the database file or want to reseed it.
* Run any Django management command inside the container with `docker-compose exec backend python3 manage.py <command>`.

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
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── emissions_project
│   ├── asgi.py
│   ├── domain
│   │   ├── entities.py
│   │   ├── __pycache__
│   │   │   ├── entities.cpython-38.pyc
│   │   │   └── repositories.cpython-38.pyc
│   │   └── repositories.py
│   ├── infrastructure
│   │   ├── management
│   │   │   └── commands
│   │   │       └── seed_emissions.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   │       ├── 0001_initial.cpython-38.pyc
│   │   │       └── __init__.cpython-38.pyc
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── models.cpython-38.pyc
│   │   │   ├── repository_impl.cpython-38.pyc
│   │   │   ├── serializers.cpython-38.pyc
│   │   │   └── views.cpython-38.pyc
│   │   ├── repository_impl.py
│   │   ├── serializers.py
│   │   └── views.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── settings.py
│   ├── tests
│   │   ├── __pycache__
│   │   │   ├── test_domain_entities.cpython-38.pyc
│   │   │   ├── test_emissions_api.cpython-38.pyc
│   │   │   ├── test_infrastructure_repository.cpython-38.pyc
│   │   │   └── test_usecases_get_emissions.cpython-38.pyc
│   │   ├── test_domain_entities.py
│   │   ├── test_emissions_api.py
│   │   ├── test_infrastructure_repository.py
│   │   └── test_usecases_get_emissions.py
│   ├── urls.py
│   ├── usecases
│   │   ├── get_emissions.py
│   │   └── __pycache__
│   │       └── get_emissions.cpython-38.pyc
│   └── wsgi.py
├── manage.py
├── project_inspect.sh
├── README.md
└── requirements.txt

```

## Testing

There are four tests in this app:
- test_domain_entities.py 
- test_emissions_api.py
- test_infrastructure_repository.py  
- test_usecases_get_emissions.py

## Running Tests

##  Tests 1
```bash
docker-compose run backend python manage.py test emissions_project.tests.test_domain_entities
```
## Test 1 Output
```bash
Found 8 test(s).
System check identified no issues (0 silenced).
........
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK

```

##  Tests 2
```bash
docker-compose run backend python manage.py test emissions_project.tests.test_emissions_api
```
## Test 2 Output
```bash
Found 6 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 0.030s

OK
```

##  Tests 3
```bash
docker-compose run backend python manage.py test emissions_project.tests.test_infrastructure_repository
```
## Test 3 Output
```bash


Found 4 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.010s

OK
```

##  Tests 4
```bash
docker-compose run backend python manage.py test emissions_project.tests.test_usecases_get_emissions
```
## Test 4 Output
```bash
Found 6 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
......
----------------------------------------------------------------------
Ran 6 tests in 0.013s

OK
```
## Development Practices
* **TDD**: Test-driven development for reliable and maintainable code.
* **Dockerized**: All dependencies are containerized for reproducible development environments.

## License
This project is open source and free to use.

## Author
**William Pérez**
* [GitHub profile](https://github.com/WilliamPerezBeltran)




