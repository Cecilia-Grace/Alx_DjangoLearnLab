# Security Hardening Summary for LibraryProject

## Settings
- DEBUG set to False in production.
- SECURE_BROWSER_XSS_FILTER, SECURE_CONTENT_TYPE_NOSNIFF and X_FRAME_OPTIONS set.
- CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE set to True (requires HTTPS).

## Templates
- All POST forms include {% csrf_token %}.

## Views and Forms
- Use Django ORM (no raw SQL); search uses filter(...__icontains=...).
- Validate user input via Django forms (BookForm).

## CSP
- Implemented Content Security Policy via django-csp (recommended).
- Alternative: Simple middleware to set CSP header.

## Testing
- Manual tests for CSRF, XSS, SQL injection and CSP header presence.

