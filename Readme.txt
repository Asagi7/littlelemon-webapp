Little Lemon Web Application - Back-End Developer Capstone
==========================================================
Django + Django REST Framework + Djoser + MySQL.
App: restaurant | Serves a static HTML page, a menu API and a
table-booking API, with user registration, token authentication and
unit tests.

SETUP
-----
1. Create the MySQL database:
       mysql -u root -p
       CREATE DATABASE littlelemon;
2. Adjust USER/PASSWORD in littlelemon/settings.py if needed.
3. pipenv shell && pipenv install
4. python manage.py makemigrations
   python manage.py migrate
5. python manage.py test restaurant        (run the unit tests)
6. python manage.py runserver

API PATHS TO TEST (with Insomnia/Postman/curl)
----------------------------------------------
Static HTML page (no auth needed):
  GET  /

User registration and authentication:
  POST /api/registration/users/           body {"username": "...", "password": "..."}
  POST /api/registration/token/login/     body {"username": "...", "password": "..."} -> {"auth_token": "..."}
  POST /api/registration/token/logout/    Authorization: Token <token>

Menu API (send header: Authorization: Token <token>):
  GET    /api/menu-items/
  POST   /api/menu-items/                 body {"title": "...", "price": 12.99, "inventory": 10}
  GET    /api/menu-items/<id>/
  PUT    /api/menu-items/<id>/            body {"title": "...", "price": 12.99, "inventory": 10}
  PATCH  /api/menu-items/<id>/            body {"price": 10.99}
  DELETE /api/menu-items/<id>/

Table booking API (Authorization: Token <token>):
  GET    /api/bookings/
  POST   /api/bookings/                   body {"name": "...", "no_of_guests": 2, "booking_date": "2026-12-13T18:00:00Z"}
  GET    /api/bookings/<id>/
  PUT    /api/bookings/<id>/
  PATCH  /api/bookings/<id>/
  DELETE /api/bookings/<id>/

Insomnia tip: after login, set the request header
  Authorization: Token <auth_token>
for all menu-items and bookings requests.
