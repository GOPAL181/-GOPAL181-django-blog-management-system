# Django Blog Management System

This is a RESTful API-based Blog Management System built using Django and Django REST Framework. It allows Admin and Blogger roles with distinct functionalities. Authentication is implemented using Django's built-in authentication system (`django.contrib.auth`), and SQLite is used as the database.

---

## Features

### Admin Features:
- Manage blogs (review and hide unwanted posts).
- Manage comments (review and hide unwanted comments).
- Manage user accounts (view, edit, and delete user accounts).

### Blogger Features:
- View and search blogs (available to unauthenticated users).
- Register and log in.
- Create, edit, and delete blog posts.
- Assign categories and tags to blog posts.
- Add, edit, and delete comments (logged-in users only).

---

## Setup Instructions

### Prerequisites
- Python 3.6+ installed on your system.
- A virtual environment tool like `virtualenv` (optional but recommended).

Development Process
1. Initial Setup:
As a beginner in Django, I started by setting up the project and understanding the structure of Django applications. I referred to official documentation and tutorials to familiarize myself with Django's Model-View-Template (MVT) architecture and REST framework.

2. Authentication:
I used Django's built-in django.contrib.auth package for user management and authentication. This saved time and provided robust functionality for login, registration, and permission management.

3. API Design:
I planned and implemented API endpoints for each feature (blogs, comments, categories, tags, and search). Serializers were used for validation and to ensure clean data handling.

4. Permissions:
Role-based access control was implemented to ensure Admin and Blogger users had appropriate permissions. Custom permissions were added for specific actions like managing blogs and comments.

5. Testing:
All endpoints were tested using Postman, and the tested collection is included in the repository as Postman_Collection.json. These tests helped identify and resolve issues during development.

6. Database:
SQLite was chosen for simplicity. Models were designed for blogs, comments, categories, and tags, with relationships to users.

7. Pagination:
Pagination was added to list endpoints to handle large datasets efficiently.

Challenges and Learning Experience
As Django is not my core skill, I faced challenges initially, especially in understanding its ORM and serializers. However, with consistent practice and documentation, I gained confidence in designing APIs, implementing permissions, and handling validations.
