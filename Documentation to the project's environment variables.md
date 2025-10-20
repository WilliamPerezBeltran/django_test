# Documentation to the project's environment variables

# Environment Variables Documentation


## Backend – Django

**Archivo:** `.env`

```env
# Django secret key 
SECRET_KEY=django-insecure-xe7nsi0b(v9nst+268w^zosr*!m%p9ke@@5bf0kcn=anncc*qo
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```

**Notas:**
- `SECRET_KEY` debe mantenerse privado y cambiarse en producción.
- `DEBUG` debe configurarse en `False` en entornos productivos.
- `DATABASE_URL` puede modificarse para usar PostgreSQL, MySQL u otro motor.
- `ALLOWED_HOSTS` define los dominios permitidos.

---

## Frontend – React

**Archivo:** `.env`

```env
API_URL=http://localhost:8000/api

DEFAULT_COUNTRY=Canada

DEFAULT_ACTIVITY=Transport

DEFAULT_EMISSION_TYPE=CO2
```

**Archivo:** `.env.development`

```env
API_URL=http://localhost:8000/api

DEFAULT_COUNTRY=Canada
DEFAULT_ACTIVITY=Transport
DEFAULT_EMISSION_TYPE=CO2
```
