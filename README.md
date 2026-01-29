# VRM / TPRM Django Backend

Django REST Framework backend for a Vendor Risk Management (VRM) / Third-Party Risk Management (TPRM) platform.  
Implements multi-tenant architecture, RBAC, Vendors module, Templates with versioning, audit logs, and scoring service integration hooks.

### Templates
- Template create
- Template version creation
- Template list & detail
- Version locked view
- Section & question structure
- Version immutability enforcement
- Audit events for create/version/publish/archive

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Docker & Docker Compose
- Celery (background jobs ready)
- Redis
- MinIO (evidence storage ready)
- OpenAPI / Swagger

---

## 🔗 Key API Endpoints

### Vendors
```
POST   /vendors
GET    /vendors
GET    /vendors/{id}
PUT    /vendors/{id}
PATCH  /vendors/{id}
```

### Templates
```
POST   /templates
POST   /templates/{id}/versions
GET    /templates
GET    /templates/{id}
GET    /templates/{id}/versions/{version_id}
```

---

## 🔌 Scoring Integration (Wired)

Trigger points added for:
- Assessment submission
- Reviewer approval
- Remediation closure

Handles timeout and safe failure behavior.

---

## 📌 Project Status

Core backend foundation complete.  
Vendors + Templates modules implemented end-to-end with RBAC, tenant isolation, and audit logs.

