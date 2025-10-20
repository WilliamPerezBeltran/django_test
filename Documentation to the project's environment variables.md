# Documentation to the project's environment variables
# Emissions Frontend

This project is an **Angular-based frontend** built to visualize and manage emission data.  

It supports multiple environments — **development**, **production**, and **Docker** — using a dynamic configuration system that generates environment variables automatically before startup.

Even though this setup is not currently being used in the production environment, it is important to have it properly configured and documented. When the project is eventually deployed to production, these environment variables and scripts will play a crucial role in ensuring that the application runs smoothly under different conditions. By maintaining a consistent structure for environment management now, you avoid potential issues later—such as misconfigured API endpoints, incorrect URLs, or missing parameters. Having this in place ahead of time guarantees that the transition from development or Docker environments to production will be seamless, secure, and easy to maintain.

Clarification: The current configuration is primarily intended for development and testing purposes. However, keeping the production environment settings prepared ensures that the system can be deployed quickly and with minimal adjustments when the production stage begins.

---

## Overview

Instead of maintaining static environment files, this project dynamically creates `src/environments/environment.ts` every time the app starts.  
This approach avoids hardcoding URLs or API keys, making the app easier to deploy in different environments.

The key file behind this logic is [`scripts/generate-env.js`](scripts/generate-env.js).  
It reads the appropriate `.env` file based on the `NODE_ENV` value, then writes its contents to the Angular environment file.

---

## How It Works

1. **When you run `npm start`:**
   - The script `prestart` executes first.
   - It runs `node scripts/generate-env.js`.
   - This script detects the environment (`NODE_ENV`) or defaults to `development`.
   - It loads the matching `.env` file, for example:
     - `.env.development`
     - `.env.production`
     - `.env.docker`
   - Then, it generates a new file at:
     ```
     src/environments/environment.ts
     ```

2. **Angular uses that generated file** at runtime to configure API URLs, country, activity, and emission type dynamically.

---

## Environment Files

Each environment file stores the variables for that context:

### `.env.development`
```bash
API_URL=http://localhost:8000/api
DEFAULT_COUNTRY=Canada
DEFAULT_ACTIVITY=Transport
DEFAULT_EMISSION_TYPE=CO2
```

---

# .env Files Setup

This section explains how to configure environment files for the project.  
Place all `.env` files in the **root directory** (next to `package.json`).

These files define environment-specific variables such as API endpoints, default country, activity, and emission type.

---

## 1. `.env.development`

Used for local development.

```bash
API_URL=http://localhost:8000/api
DEFAULT_COUNTRY=Canada
DEFAULT_ACTIVITY=Transport
DEFAULT_EMISSION_TYPE=CO2
```

---

## 2. `.env.production`

Used for the production environment.

```bash
API_URL=https://your-production-domain.com/api
DEFAULT_COUNTRY=Canada
DEFAULT_ACTIVITY=Transport
DEFAULT_EMISSION_TYPE=CO2
```

---

## 3. `.env.docker` (optional)

Used when running the app in a Docker container.

```bash
API_URL=http://backend:8000/api
DEFAULT_COUNTRY=Canada
DEFAULT_ACTIVITY=Transport
DEFAULT_EMISSION_TYPE=CO2
```

# Create Environment Files

Run these commands from the root of the project (next to your `package.json`).

## 1. Development environment

```bash
echo "API_URL=http://localhost:8000/api
DEFAULT_COUNTRY=Canada
DEFAULT_ACTIVITY=Transport
DEFAULT_EMISSION_TYPE=CO2" > .env.development
```

## 2. Production environment

```bash
echo "API_URL=https://your-production-domain.com/api
DEFAULT_COUNTRY=Canada
DEFAULT_ACTIVITY=Transport
DEFAULT_EMISSION_TYPE=CO2" > .env.production
```

## 3. Docker environment

```bash
echo "API_URL=http://backend:8000/api
DEFAULT_COUNTRY=Canada
DEFAULT_ACTIVITY=Transport
DEFAULT_EMISSION_TYPE=CO2" > .env.docker
```

---

## Notes

Run these commands from your terminal inside the project root directory.  

After running them, you should see the three `.env` files when you list the directory:

```bash
ls -a
```

You can verify each file’s content with:

```bash
cat .env.development
```


## Notes

- Each `.env` file corresponds to a different deployment environment.  
- The correct file is selected automatically based on the value of the `NODE_ENV` variable.  
- Make sure these files are **not committed** to version control if they contain sensitive information.
