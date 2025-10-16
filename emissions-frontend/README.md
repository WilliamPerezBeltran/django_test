# Emissions Frontend

This document provides an overview of the Emissions frontend project. It includes architecture, design principles, components, services, testing practices, and Docker setup. This README is intended for developers and engineers who want to understand, run, and extend the frontend application.

## Project Description

The Emissions frontend is an Angular application that visualizes emissions data from different countries, years, and activities. It consumes a REST API to fetch data and renders charts using `@swimlane/ngx-charts` and `d3`. The project is structured for modularity and maintainability:

- **Components**: UI elements like `EmissionsChartComponent`.
- **Services**: Handle API communication (`EmissionsService`).
- **Models**: Define TypeScript interfaces for domain entities (`Emission`).
- **Styles**: Sass (`.scss`) is used for component styling.
- **Tests**: Unit tests using Jasmine and Karma.

This architecture ensures separation of concerns, reusability, and testability.

## Stack

- Angular 20
- TypeScript 5.9
- RxJS 7
- ngx-charts 23
- D3 7
- Sass / SCSS
- Docker & Docker Compose

## Architecture Explanation

- **Components**: Display UI and interact with services. Each component has its own template and styles.
- **Services**: Responsible for API calls and data handling.
- **Models**: Define strong typing for domain objects.
- **Modules**: Organize components and services.
- **Testing**: Jasmine + Karma unit tests for components and services.

This separation ensures **Single Responsibility Principle (SRP)** and allows adding features without modifying existing components (**Open/Closed Principle**).

## SOLID Principles Applied

- **SRP**: Each component or service has a single responsibility.
- **OCP**: Components can be extended with additional functionality without modifying existing code.
- **LSP**: Components and services can be replaced by compatible alternatives.
- **ISP**: Services expose only the methods required by components.
- **DIP**: Components depend on service abstractions rather than concrete implementations.

## Design Patterns

- **Service Pattern**: Angular services handle API requests and data manipulation.
- **Component-Based Architecture**: Components encapsulate templates, styles, and behavior.
- **Observable Pattern**: RxJS observables handle asynchronous data streams.

## Project Structure

```tree
.
├── angular.json
├── dist
│   └── test-out
├── docker-compose.yml
├── Dockerfile
├── package.json
├── package-lock.json
├── public
│   └── favicon.ico
├── README.md
├── src
│   ├── app
│   │   ├── app.component.html
│   │   ├── app.component.scss
│   │   ├── app.component.ts
│   │   ├── app.config.ts
│   │   ├── components
│   │   │   └── emissions-chart
│   │   │       ├── emissions-chart.component.html
│   │   │       ├── emissions-chart.component.scss
│   │   │       └── emissions-chart.component.ts
│   │   ├── models
│   │   │   └── emission.model.ts
│   │   └── services
│   │       └── emissions.service.ts
│   ├── assets
│   ├── index.html
│   ├── main.ts
│   └── styles.scss
├── tsconfig.app.json
├── tsconfig.json
└── tsconfig.spec.json
```

### Folder Description

- `app/components/` -> Angular components (UI elements like charts).
- `app/services/` -> Angular services for API requests.
- `app/models/` -> TypeScript interfaces and domain models.
- `assets/` -> Static assets like images or icons.
- `tests/` -> Jasmine and Karma tests.

### File Description

- `emissions-chart.component.ts` -> Component logic for displaying emission charts.
- `emissions-chart.component.html` -> Component template.
- `emissions-chart.component.scss` -> Component styles.
- `emission.model.ts` -> TypeScript interface for Emission entity.
- `emissions.service.ts` -> Service to fetch emissions from API.
- `app.component.ts` -> Main app component logic.
- `app.component.html` -> Main template.
- `app.component.scss` -> Main styles.

## Docker Setup

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
The project uses **Jasmine** and **Karma**.
Run all tests:

```bash
npm run test
```
Run tests in watch mode:

```bash
npm run test -- --watch
```

## Development Practices

- **Component-Based Architecture**: Keep UI modular and reusable.
- **Service-Oriented**: API communication is centralized in services.
- **Test-Driven Development**: Use Jasmine/Karma for unit tests.
- **Dockerized**: Ensure consistent development environments.
- **Linting**: Prettier enforces code style.

## Author

**William Pérez**

- [GitHub profile](https://github.com/WilliamPerezBeltran)
