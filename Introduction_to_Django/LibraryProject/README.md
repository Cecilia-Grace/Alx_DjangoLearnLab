# 📚 LibraryProject - Django Development Environment Setup

This repository contains the foundational setup for the **LibraryProject**, created as part of an exercise to gain familiarity with the basic workflow of a Django project, including environment setup and running the development server.
## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Ensure Python is installed.**
2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install Django:**
    ```bash
    pip install django
    # Note: To document dependencies, run: pip freeze > requirements.txt
    ```
4.  **Create the Django Project:**
    (Note: This step is already complete, but included for documentation.)
    ```bash
    django-admin startproject LibraryProject
    ```
## Running the Development Server

1.  Navigate into the main project directory:
    ```bash
    cd LibraryProject
    ```
2.  Start the server:
    ```bash
    python manage.py runserver
    ```
3.  Open your browser and navigate to: **http://127.0.0.1:8000/**
    (The default Django welcome page should be visible.)
## Key Project Components

The core configuration files are located inside the inner `LibraryProject` directory:

* **`manage.py`**: A command-line utility for interacting with the project (e.g., running the server, migrations).
* **`settings.py`**: Contains all project-level configuration, such as database settings (SQLite is the default), installed apps, and static files.
* **`urls.py`**: The project's main URL configuration, acting as the "table of contents" for the entire site.
