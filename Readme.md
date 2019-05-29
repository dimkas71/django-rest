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

13.1 https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html

14. pip install djangorestframework_simplejwt
15. update token http post http://127.0.0.1:8000/api/token/ username=admin password=password123
16. request to url
    http http://127.0.0.1:8000/hello/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTU5MTM3NjE4LCJqdGkiOiIyYjE3OGE1Yzg4YWE0Y2U5OTg2YzEwMGQ0NzEwMzM0OSIsInVzZXJfaWQiOjF9.odpaw2bYk_0rqrcEEVl7GWDYHQF-Q7XzsCqwl4_b_Zs"

17. create db demo and load data from a sql script
17.1 sudo -u postgres psql -d demo
17.2 \i <path to sql file>

18. setup postgresql connection
18.1 install postgres driver psycopg2
    sudo apt install postgresql-server-dev-9.5
    sudo apt install libpq-dev
    pip install psycopg2-binary #  or     pip install psycopg2
18.2 Generating models from db
    python3.7 manage.py inspectdb 
  
