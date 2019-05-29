0. https://www.django-rest-framework.org/tutorial/quickstart/ - tutorial

1. python -m venv venv
2. venv\Scripts\activate.bat
3. pip install httpie
4. python -m install --upgrade pip 
5. pip install django
6. pip install djangorestframework
7. django-admin startproject flightsrest .
8. cd flightsrest 
9. django-admin startapp flightsrest
10. python manage.py migrate
11. python manage.py createsuperuser --email admin@example.com --username admin 
    password:password123
12. python manage.py runserver
13. http -a admin:password123 http://127.0.0.1:8000/users/ 


