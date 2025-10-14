# Emissions Project

This document provides an overview of the complete Emissions project, including the backend and frontend. It includes architecture, design principles, API endpoints, testing practices, and Docker setup. This README is intended for developers and engineers who want to understand, run, and extend the application.

## Project Description

The Emissions project manages emission data for different countries, years, and activities. The backend exposes this data via a REST API, and the frontend visualizes it using Angular and `ngx-charts`. The project is structured to separate domain logic, infrastructure, and presentation layers:

* **Backend**:

  * **Domain**: Entities (`Emission`) and abstract repositories (`EmissionRepository`) that define core business logic.
  * **Infrastructure**: Django models, serializers, views, and repository implementations.
  * **Use Cases**: Application logic such as fetching emissions.
  * **Tests**: Validates the behavior of domain, infrastructure, and use cases.
  * **README**: See `emissions-backend/README.md` for detailed backend information, endpoints, and testing instructions.

* **Frontend**:

  * Angular app to visualize emission data with interactive charts.
  * Service layer communicates with the backend API.
  * Components display emissions data by country, year, and activity.
  * **README**: See `emissions-frontend/README.md` for detailed frontend setup, components, and testing instructions.

This architecture ensures modularity, testability, and maintainability.

## Development Practices

* **TDD**: Test-driven development for reliable and maintainable code.
* **Dockerized**: All dependencies are containerized.
* **Code Quality**: PEP8 and Pythonic standards in backend; ESLint and Prettier for frontend.
* **CI/CD Ready**: Can be integrated with GitHub Actions for automated testing.

## Author

**William Pérez**  
[GitHub profile](https://github.com/WilliamPerezBeltran)
