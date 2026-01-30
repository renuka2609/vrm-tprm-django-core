# Django Backend – P0 Modules + Dashboard

Django + DRF backend foundation for a multi-tenant assessment platform with RBAC, audit logging, and workflow enforcement.

## Modules
- Assessments – assign, list, detail, template lock
- Responses – draft save, final submit, lock
- Evidence – upload, map to question, expiry, download
- Reviews – reviewer decision, scoring trigger
- Remediations – create, vendor response, closure
- Dashboard – stats + activity feed
- Audit Logs – all critical actions tracked

## Security
- RBAC permissions
- Tenant isolation
- Cross-tenant blocked (403)
- Invalid transitions (409)

## Setup
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py createsuperuser  
python manage.py runserver  

## APIs
- `/dashboard/stats/` → counts summary
- `/dashboard/activity/` → audit activity feed
- Swagger → `/swagger/`

## Notes
- Always filter by tenant_id  
- Enforce roles on every endpoint  
- Log audit events for write actions  
- Lock records after final submission  
