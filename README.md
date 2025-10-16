# Emissions Project

This repository contains the full Emissions project, including backend and frontend applications, detailed documentation, and technical test materials. The project is structured to separate concerns clearly and provide comprehensive guidance for developers.

## Repository Structure

```
.
├── docs
├── emissions-backend
├── emissions-frontend
├── README.md
├── backend-documentation.pdf
├── frontend-documentation.pdf
├── Technical Test, Colombia.pdf
```

### Folders Overview

* **docs**
  Includes supplementary reference materials, notes, and supporting documentation, along with the technical test file for the project. A **video demonstrating** the code's results is also provided.

* **emissions-backend**
  This folder contains the Django-based backend application responsible for managing, storing, and exposing emission data.

  * Includes its own `README.md` with detailed instructions on setup, running the server, database configuration, and testing.
  * Includes `backend-documentation.pdf` for an in-depth technical overview of architecture, entities, use cases, and API endpoints.

* **emissions-frontend**
  This folder contains the Angular-based frontend application responsible for displaying emission data, handling user interaction, and communicating with the backend.

  * Includes its own `README.md` with detailed instructions on project setup, building, running, and testing the frontend application.
  * Includes `frontend-documentation.pdf` for an in-depth technical overview of components, services, state management, and UI structure.

### Documentation Files

* **backend-documentation.pdf**
  Comprehensive documentation for the backend, detailing architecture, design, APIs, database schema, and testing practices.

* **frontend-documentation.pdf**
  Comprehensive documentation for the frontend, detailing UI components, state management, services, routing, and integration with the backend.

* **Technical Test, Colombia.pdf**
  Contains the technical test instructions, requirements, and specifications used during the project evaluation phase. A copy of this file is also available in the `docs` folder.

### Notes

* Each folder (`emissions-backend` and `emissions-frontend`) is self-contained with its own README and PDF documentation.
* Developers should first review the respective folder README for setup instructions before running or modifying the applications.
* PDFs provide deeper insights into design decisions, architecture, and technical details for both backend and frontend.

> **Important Note:**  
> This API was developed as a simple demonstration and does not implement standard security measures. Authentication, authorization, encryption, rate limiting, and other best practices for securing RESTful APIs have not been applied. All data is openly accessible, and the API should not be used in a production environment without proper security controls.


## Author

**William Pérez**  
[GitHub profile](https://github.com/WilliamPerezBeltran)
