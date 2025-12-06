Django Authentication System

A simple user authentication system built with Django, featuring:

User Registration (with email)

Login & Logout

Profile View & Edit

CSRF-protected forms

Secure password handling with Django’s hashing

URL Paths
Path	Purpose
/login/	Login
/logout/	Logout
/register/	Registration
/profile/	Profile management
Usage

Register a new user at /register/

Login at /login/

Edit your profile at /profile/

Logout at /logout/

Security

CSRF protection enabled for all forms

Passwords hashed securely using Django’s default algorithms

Profile pages require login