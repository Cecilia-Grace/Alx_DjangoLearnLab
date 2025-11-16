# Permissions & Groups Setup (Bookshelf App)

✔ Custom permissions added to Book model:
    - can_view
    - can_create
    - can_edit
    - can_delete

✔ Groups created and permissions assigned in Django Admin:
    - Viewers → can_view
    - Editors → can_view, can_edit, can_create
    - Admins → Full permissions

✔ Views protected using @permission_required decorator

